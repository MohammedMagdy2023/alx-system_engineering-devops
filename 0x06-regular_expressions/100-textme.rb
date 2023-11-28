#!/usr/bin/env ruby
ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).each { |match| puts match.join(',') }
