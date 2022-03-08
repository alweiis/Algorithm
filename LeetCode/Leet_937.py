class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        sorted_logs, digit_log = [], []
        for log in logs:
            chk = log.split()
            if chk[1].isalpha():
                sorted_logs.append(log)
            else:
                digit_log.append(log)
        sorted_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        sorted_logs.extend(digit_log)
        return sorted_logs