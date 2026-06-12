import psutil
import logging

class SentryModule:
    def __init__(self):
        self.logger = logging.getLogger("Sentry")

    def monitor_environment(self):
        # Scan for active processes relevant to your work
        running_procs = [p.name().lower() for p in psutil.process_iter()]
        
        if "chromedriver.exe" in running_procs:
            return "Automation environment detected. Initiating QA monitoring."
        if "gps_service.exe" in running_procs: # Hypothetical
            return "Hardware detected. Monitoring telemetry stream."
        
        return "System idle."