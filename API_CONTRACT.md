# API Contract - Smart Irrigation

## 1. Sensor Data (From ESP32/Simulator to Backend)
**Endpoint:** `POST /api/data`
**Format:**
```json
{
  "sensor_id": "ESP32_01",
  "moisture": 45.5,
  "temperature": 24.0,
  "humidity": 60,
  "timestamp": "2024-05-20T10:00:00Z"
}
