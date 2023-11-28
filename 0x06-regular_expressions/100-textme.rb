#!/usr/bin/env ruby
puts ARGV[0].scan(//(\[from:?\+\d{1,}\]|\[from:\w{1,}\]) (\[to:?\+\d{1,}\]|\[to:\w{1,}\]) \[flags:(.*?)\]).join
