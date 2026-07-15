import axios from "axios";

const API = "http://localhost:8000";

export async function getHealth() {
    const response = await axios.get(`${API}/health`);
    return response.data;
}

export async function executeTask(task) {
    const response = await axios.post(
        `${API}/execute`,
        null,
        {
            params: {
                task: task
            }
        }
    );
    return response.data;
}
