# import re
# from collections import defaultdict

# class SecurityLogAnalyzer:
#     def __init__(self, log_file):
#         self.log_file = log_file
#         self.failed_logins = defaultdict(int)
#         self.sensitive_access = defaultdict(int)

#     def analyze_logs(self):
#         with open(self.log_file, 'r') as file:
#             for line in file:
#                 self.process_line(line)

#     def process_line(self, line):
#         # Regex patterns
#         failed_login_pattern = r'ERROR Failed login attempt for user (.+)'
#         sensitive_data_pattern = r'User  (.+) accessed sensitive data: \[(.+)\]'

#         # Check for failed login attempts
#         failed_login_match = re.search(failed_login_pattern, line.strip())
#         if failed_login_match:
#             user = failed_login_match.group(1)
#             self.failed_logins[user] += 1

#         # Check for access to sensitive data
#         sensitive_data_match = re.search(sensitive_data_pattern, line.strip())
#         if sensitive_data_match:
#             user, sensitive_info = sensitive_data_match.groups()
#             self.sensitive_access[user] += 1
#             print(f"User  {user} accessed sensitive data: {sensitive_info}")

#     def report(self):
#         print("\nFailed Login Attempts Report:")
#         for user, count in sorted(self.failed_logins.items(), key=lambda x: x[1], reverse=True):
#             print(f"User {user}, Failed Attempts: {count}")

#         print("\nSensitive Data Access Report:")
#         for user, count in sorted(self.sensitive_access.items(), key=lambda x: x[1], reverse=True):
#             print(f"User {user}, Access Count: {count}")


# def main():
#     log_file_path = "C:\\Users\\daryl\\OneDrive\\DMB\\Python\\ran_project krypton_logs_20250407.txt"  # Adjust this path as needed
#     analyzer = SecurityLogAnalyzer(log_file_path)
#     analyzer.analyze_logs()
#     analyzer.report()

# if __name__ == "__main__":
#     main()


import re
from collections import defaultdict

class SecurityLogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.failed_logins = defaultdict(int)
        self.sensitive_access = defaultdict(int)

    def analyze_logs(self):
        with open(self.log_file, 'r') as file:
            for line in file:
                self.process_line(line)

    def process_line(self, line):
        # Regex patterns
        failed_login_pattern = r'ERROR Failed login attempt for user (\w+)'
        sensitive_data_pattern = r'INFO User (\w+) accessed sensitive data'

        # Check for failed login attempts
        failed_login_match = re.search(failed_login_pattern, line.strip())
        if failed_login_match:
            user = failed_login_match.group(1)
            self.failed_logins[user] += 1

        # Check for access to sensitive data
        sensitive_data_match = re.search(sensitive_data_pattern, line.strip())
        if sensitive_data_match:
            user = sensitive_data_match.group(1)
            self.sensitive_access[user] += 1
            # print(f"User {user} accessed sensitive data.")

    def report(self):
        print("\nFailed Login Attempts Report:")
        for user, count in sorted(self.failed_logins.items(), key=lambda x: x[1], reverse=True):
            print(f"User {user}, Failed Attempts: {count}")

        print("\nSensitive Data Access Report:")
        for user, count in sorted(self.sensitive_access.items(), key=lambda x: x[1], reverse=True):
            print(f"User {user}, Access Count: {count}")


def main():
    log_file_path = "C:\\Users\\daryl\\OneDrive\\DMB\\Python\\ran_project krypton_logs_20250407.txt"
    analyzer = SecurityLogAnalyzer(log_file_path)
    analyzer.analyze_logs()
    analyzer.report()

if __name__ == "__main__":
    main()