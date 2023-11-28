#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(?P<sender>.*?\] \[to:<?P<reciever>.*?\] \[flags:<?P<flags>.*?\]/)
