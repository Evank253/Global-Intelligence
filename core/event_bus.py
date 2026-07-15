"""
KCN Intelligence OS - Event Bus
Publish-subscribe message bus for asynchronous and synchronous intra-system communication and observability.
"""

import time
import logging
import uuid
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Any, Optional

logger = logging.getLogger("KCN.EventBus")


@dataclass
class Event:
    topic: str
    payload: Dict[str, Any]
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    sender: str = "system"
    timestamp: float = field(default_factory=time.time)


class EventBus:
    """Central event bus supporting pub/sub and full audit history."""

    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Event], None]]] = {}
        self._global_subscribers: List[Callable[[Event], None]] = []
        self._event_history: List[Event] = []
        self._max_history = 1000

    def subscribe(self, topic: str, handler: Callable[[Event], None]) -> None:
        """Subscribe a handler to a specific topic."""
        if topic not in self._subscribers:
            self._subscribers[topic] = []
        self._subscribers[topic].append(handler)
        logger.debug(f"Subscribed handler to topic: {topic}")

    def subscribe_all(self, handler: Callable[[Event], None]) -> None:
        """Subscribe a handler to all events across topics."""
        self._global_subscribers.append(handler)

    def publish(self, topic: str, payload: Dict[str, Any], sender: str = "system") -> Event:
        """Publish an event to subscribers and log in history."""
        event = Event(topic=topic, payload=payload, sender=sender)
        
        # Keep bounded history
        self._event_history.append(event)
        if len(self._event_history) > self._max_history:
            self._event_history.pop(0)

        # Notify topic-specific subscribers
        if topic in self._subscribers:
            for handler in self._subscribers[topic]:
                try:
                    handler(event)
                except Exception as e:
                    logger.error(f"Error handling event {event.event_id} on {topic}: {e}")

        # Notify global subscribers
        for handler in self._global_subscribers:
            try:
                handler(event)
            except Exception as e:
                logger.error(f"Error handling event {event.event_id} in global handler: {e}")

        return event

    def get_history(self, topic_filter: Optional[str] = None, limit: int = 50) -> List[Dict[str, Any]]:
        """Retrieve recent events, optionally filtered by topic."""
        events = self._event_history
        if topic_filter:
            events = [e for e in events if e.topic == topic_filter]
        
        recent = events[-limit:]
        return [
            {
                "event_id": e.event_id,
                "topic": e.topic,
                "sender": e.sender,
                "timestamp": e.timestamp,
                "payload": e.payload,
            }
            for e in recent
        ]

    def clear(self) -> None:
        """Clear history and reset subscribers."""
        self._subscribers.clear()
        self._global_subscribers.clear()
        self._event_history.clear()
