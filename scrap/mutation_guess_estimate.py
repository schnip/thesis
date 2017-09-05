char_cnt = 112
chars_available = 128

# No single removal can make the code work perfectly
sing_rem = 0
sing_rem_prob = sing_rem / char_cnt

# Single add can fix it by adding a comment
# I cannot think of any other ways that it can be done with a single add
sing_add = 3
sing_add_prob = sing_add / (char_cnt * chars_available)

# Swap the 1 to a 0
# Swap two of the different ones to a hash
# Swap plus to mult
# Swap plus to divide
sing_swap = 1 + 2 + 1 + 1
sing_swap_prob = sing_swap / (char_cnt * chars_available)

total_prob = (sing_rem_prob + sing_add_prob + sing_swap_prob) / 3

print(total_prob)