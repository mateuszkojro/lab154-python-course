#include <cstddef>
#include <iostream>
#include <map>
#include <string>
#include <vector>

std::vector<std::string> SplitBy(const std::string &string,
                                 const char separator) {
  std::vector<std::string> lines;
  std::string letters_since_separator;

  for (int i = 0; i < string.size(); i++) {
    char current_character = string[i];
    if (current_character == separator) {
      lines.push_back(letters_since_separator);
      letters_since_separator = "";
    } else {
      letters_since_separator += string[i];
    }
  }
  lines.push_back(letters_since_separator);
  return lines;
}

std::vector<std::string> SplitLines(const std::string &line) {
  return SplitBy(line, '\n');
}

std::vector<std::string> SplitColumns(const std::string &column) {
  return SplitBy(column, ',');
}

std::map<std::string, std::vector<std::string>>
ParseCSV(const std::string &file_content) {

  std::map<std::string, std::vector<std::string>> parsed_file;

  auto lines = SplitLines(file_content);
  auto headers = SplitColumns(lines[0]);

  for (const auto &header : headers) {
    parsed_file[header] = {};
  }

  for (size_t i = 1; i < lines.size(); i++) {
    auto line = lines[i];
    std::vector<std::string> fields = SplitColumns(line);
    for (size_t j = 0; j < fields.size(); j++) {
      std::string field = fields[j];
      std::string header = headers[i];
      parsed_file[header].push_back(field);
    }
  }

  return parsed_file;
}

int main() {
  std::string input = "A,B,C\naa,1,1.1\nbb,2,2.2\ncc,3,3.3";
  auto parsed_file = ParseCSV(input);
  for (const auto &[column, values] : parsed_file) {
    std::cout << column << "={";
    for (const auto &value : values) {
      std::cout << value << ",";
    }
    std::cout << "}";
  }
}