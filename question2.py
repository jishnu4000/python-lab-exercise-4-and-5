from abc import ABC, abstractmethod
import math

class DataAnalyzer(ABC):
  @abstractmethod
  def analyze():
    pass

class AnalysisError(Exception):
  "Raised when there is an unexpected error in analysis"
  pass

class TextDataAnalyzer(DataAnalyzer):
  def analyze(self, data):
    try:
      if isinstance(data, list):
        if not all(isinstance(i, str) for i in data):
          raise TypeError("Expected a list of strings for text analysis")
        print(f"Concatenated string: {' '.join(data)}")

      else:
        if not isinstance(data, str):
          raise TypeError("Expected a string for text analysis")
        print(f'Number of words: {len(data.split())}')

    except Exception as e:
      print(f"Unexpected error in TextDataAnalyzer: {e}")
      raise AnalysisError("Error in analyzing text data") from e

class NumericDataAnalyzer(DataAnalyzer):
  def analyze(self, data):
    try:
      if isinstance(data, list):
        if not all(isinstance(i, (int, float)) for i in data):
          raise TypeError("Expected a list of numeric values for analysis")
        else:
          print(f'Sum of values: {sum(data)}, Maximum value: {max(data)}, Minimum value: {min(data)}')

      else:
        if not isinstance(data, (int, float)):
          raise TypeError("Expected a numeric value for analysis")
        if data < 0:
          raise ValueError("Numeric data must be non-zero and positive")
        print(f'Square of value:{math.pow(data, 2)}, Square root of value: {math.sqrt(data)}, Factorial of value: {math.factorial(data)}')

    except Exception as e:
      print(f"Unexpected error in NumericDataAnalyzer: {e}")
      raise AnalysisError("Error in analyzing numeric data") from e

if __name__ == '__main__':
  analyzers = [
    TextDataAnalyzer(),
    NumericDataAnalyzer()
  ]

  sample_data = [
    "Sample string text for analysis testing",
    10.5,
    [21, 42, 13, 4, 85],
    ["str1", "str2", "str3", "aaaaa"],
  ]

  for a in analyzers:
    for s in sample_data:
      try:    
        a.analyze(s)
        print()
      except Exception as e:
        print(e)