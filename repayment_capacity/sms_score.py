#!/usr/bin/env python
import csv;

bad_keywords = ["is overdue",
"has bounced",
"bounce",
"has not been honoured",
"severely overdue",
"is still pending",
"overdue hai",
"overdue of",
"despite several reminders",
"is still due",
"is still unpaid",
"payment overdue",
"overdues",
"is unpaid",
"remains unpaid",
"is outstanding",
"in overdue",
"have not received",
"still not received",
"are overdue",
"towards overdue"
]

def sms_score(sms):
    for keyword in bad_keywords:
        if (keyword in sms.lower()):
            return 0
    return 1

def calculate_sms_score(all_sms):
    total_score = 0;
    for sms in all_sms:
        total_score += sms_score(sms)
    return total_score/len(all_sms)*10
