#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python code that simulates a dictionary based on a json file and online API.
data.json is a json file that contains a dictionary of words and their meanings.
"""

from b_online_dictionary.requests import take_argument, search_word,internet_checker, redirect_to_offline

if __name__ == "__main__":
    if internet_checker():
        target_word = take_argument()
        result = search_word(target_word)
        print(result)
    else:
        redirect_to_offline()