"""
KCN-AKIIS Subpackage - Evaluation & Immune System Backbone (Phases 96, 100).
Teacher/Student training, global benchmark sweepers, failure ledgers, and immune audit reports.
"""

from kcn_akiis.teacher_student import TeacherStudentSystem
from kcn_akiis.benchmark_engine import BenchmarkEngine
from kcn_akiis.performance_report import PerformanceReportGenerator

__all__ = ["TeacherStudentSystem", "BenchmarkEngine", "PerformanceReportGenerator"]
