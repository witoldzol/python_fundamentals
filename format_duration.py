import unittest


def print_duration(durations):
    output = ''

    for i, k in enumerate(durations):
        time_chunk = f'{durations[k]} {k}'

        if durations[k] > 1:
            time_chunk += 's'

        if i == (len(durations) - 2):
            time_chunk += ' and '
        elif i < (len(durations) - 2):
            time_chunk += ', '

        output += time_chunk
    return output


def format_duration(seconds):
    times = [("year", 365 * 24 * 60 * 60),
             ("day", 24 * 60 * 60),
             ("hour", 60 * 60),
             ("minute", 60),
             ("second", 1)]

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs
    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]


# def format_duration(seconds):
#     if not seconds:
#         return 'now'
#
#     minute = 60
#     hour = 60 * minute
#     day = 24 * hour
#     year = 365 * day
#
#     durations = dict()
#
#     y = seconds // year
#     if y > 0:
#         durations['year'] = y
#     seconds -= (year * y)
#
#     d = seconds // day
#     if d > 0:
#         durations['day'] = d
#     seconds -= (day * d)
#
#     h = seconds // hour
#     if h > 0:
#         durations['hour'] = h
#     seconds -= (hour * h)
#
#     m = seconds // minute
#     if m > 0:
#         durations['minute'] = m
#     seconds -= (minute * m)
#
#     if seconds > 0:
#         durations['second'] = seconds
#
#     return print_duration(durations)


class TestFormatDuration(unittest.TestCase):
    def test_duration(self):
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")
