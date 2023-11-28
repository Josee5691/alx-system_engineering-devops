#!/usr/bin/env ruby
log_entries.each { |entry| match = entry.match(/\[from:(?<sender>.*?)\] \[to:(?<receiver>.*?)\] \[flags:(?<flags>.*?)\]/); puts "#{match[:sender]},#{match[:receiver]},#{match[:flags]}" if match }

