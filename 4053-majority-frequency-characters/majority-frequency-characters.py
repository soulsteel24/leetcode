class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        
        freq_group = defaultdict(list)
        for char, freq in count.items():
            freq_group[freq].append(char)
        
        best_freq = -1
        max_size = -1

        for freq, chars in freq_group.items():
            size = len(chars)
            if size > max_size or (size == max_size and freq>best_freq):
                max_size = size
                best_freq = freq
        return "".join(freq_group[best_freq])
