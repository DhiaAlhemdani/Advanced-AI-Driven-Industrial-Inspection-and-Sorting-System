# Monitoring implementation boundary

Place the **original** MQTT publisher/subscriber, dashboard, and predictive-maintenance analysis files here when they are supplied. Record broker configuration through environment variables or a redacted example; never commit credentials.

The public Kaggle notebook supplies an original host-side monitoring implementation with MQTT topics, a Dash/Plotly dashboard, Flask MJPEG video, a defect-source rule engine, and a heuristic predictive-maintenance model. The exact notebook export is still pending. Treat its `localhost` endpoints, simulation defaults, thresholds, payloads, and sensor assumptions as source configuration until they are extracted, tested, and documented with the corresponding benchmark logs.
