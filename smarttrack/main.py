# main.py - Entry point for the SmartTrack application

import sys
from smarttrack.contract_monitor import start_monitoring
from smarttrack.analytics import analyze_contracts

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "monitor":
            start_monitoring()
        elif command == "analyze":
            analyze_contracts()
        else:
            print("Invalid command. Use 'monitor' or 'analyze'.")
    else:
        print("Please provide a command: 'monitor' or 'analyze'.")

if __name__ == "__main__":
    main()
