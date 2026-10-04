# Configuration boundary

Store non-secret, versioned configuration here when the original implementation is added. Keep credentials and deployment-specific hostnames in environment variables or a local ignored file. Every configuration used for a benchmark should be copied or hashed in the corresponding result record so the experiment can be reproduced.

Known project components are the computer-vision inspection, Arduino Mega 2560/dual-servo sorting, MQTT transport, dashboard, and predictive-maintenance monitoring. Exact runtime values are not yet evidenced in this checkout.
