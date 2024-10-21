import re
from typing import List, Any

def check_data_quality_by_threshold(corrupted_records_count: int,
                                    total_records_count: int,
                                    description: str) -> bool:
    """
    Evaluates the percentage of problematic records against a threshold and
    returns whether checked rule meets the criteria.
    :param corrupted_records_count: Number of records that do not meet quality criteria.
    :param total_records_count: Total number of records evaluated.
    :param description: Description of the check being performed for logging purposes.
    :return: True if the corrupt ratio is within acceptable limits, otherwise False.
    """
    percentage = (corrupted_records_count / total_records_count) * 100
    print(f"{description}: {percentage}% corrupted.")
    return percentage <= 5


def check_for_completeness(records: List[str]) -> bool:
    """
    Checks dataset completeness, ensuring no entries are null or empty.
    :param records: List of records.
    :return: True if no incomplete records found, False otherwise.
    """
    incomplete_count = sum(1 for record in records if record is None or record == '')
    return check_data_quality_by_threshold(incomplete_count, len(records), "Completeness check")


def check_maximum_length(records: List[str], max_length: int) -> bool:
    """
    Checks that no entry in the data is above the allowed maximum length.
    :param records: List of string records.
    :param max_length:: Maximum allowed length for any record.
    :return: True if all records meet the length requirement, False otherwise.
    """
    excess_length_count = sum(1 for record in records if len(record) > max_length)
    return check_data_quality_by_threshold(excess_length_count, len(records), f"Maximum length check for ({max_length} characters)")


def check_allowed_values(records: List[str], allowed_values: List[Any]) -> bool:
    """
    Checks that each entry in the dataset is one of the allowed values.
    :param records: List of records.
    :param allowed_values: List containing allowable values.
    :return: True if all records contain only allowed values, False otherwise.
    """
    disallowed_count = sum(1 for record in records if record not in allowed_values)
    return check_data_quality_by_threshold(disallowed_count, len(records), "Allowed values check")


def check_uniqueness(records: List[str]) -> bool:
    """
    Checks uniqueness across all records ensuring no duplicates exist.
    :param records: List of records.
    :return: True if all records are unique, False otherwise.
    """
    unique_records = set(records)
    duplicate_count = len(records) - len(unique_records)
    return check_data_quality_by_threshold(duplicate_count, len(records), "Uniqueness check")


def check_regex_patterns(records: List[str], pattern: str) -> bool:
    """
    Verifies that all records match a provided regex pattern.
    :param records: List of string records.
    :param pattern: Regex pattern to match against each record.
    :return: True if all records match the pattern, False otherwise.
    """
    pattern_re = re.compile(pattern)
    mismatches = [record for record in records if not pattern_re.match(record)]
    mismatch_count = len(mismatches)
    if mismatch_count > 0:
        print("Mismatched records:", mismatches[:10])  # Display up to the first 10 mismatches
    return check_data_quality_by_threshold(mismatch_count, len(records), f"Regex pattern matches ({pattern}) check")


def check_positive_values(records: List[str]) -> bool:
    """
    Ensures that all numeric entries are positive.
    :param records: List of numeric records.
    :return: True if all records are positive, False otherwise.
    """
    negative_or_zero_count = sum(1 for record in records if record <= 0)
    return check_data_quality_by_threshold(negative_or_zero_count, len(records), "Positive values check")
