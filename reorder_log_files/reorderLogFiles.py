class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs) <= 1:
            return logs

        result = []
        letter_logs = []
        digit_logs = []

        for i, log in enumerate(logs):
            split_log = (word for word in log.split())
            prefix = next(split_log)
            rest = " ".join(w for w in split_log)

            if rest[0].isnumeric():
                # remember in which order digit logs were stored
                digit_logs.append(i)
            else:
                letter_logs.append((prefix, rest))

        result += [k + ' ' + v for (k, v) in sorted(letter_logs, key=lambda x: x[1] + x[0])]
        result += [logs[i] for i in digit_logs]
        return result
