def fibonacci(n):
  return 1 if n in [1, 2] else ((fibonacci(n - 2)) + fibonacci(n - 1))
