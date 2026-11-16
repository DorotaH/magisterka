def Seq_Linear(seq_nums):
  seq_nums = [seq_nums[x] - seq_nums[x - 1] for x in range(1, len(seq_nums))]
  return "Linear Sequence" if len(set(seq_nums)) == 1 else "Non Linear Sequence"
