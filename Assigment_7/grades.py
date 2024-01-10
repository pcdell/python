def sort_grades(records):
    def sorting_key(record):
        name, number, grades = record
        average_grade = sum(grades) / len(grades) if grades else 0
        return (-average_grade, name, number)

    return sorted(records, key=sorting_key)