# Python 3.7
import click
import json
import urllib.parse
import os
import errno


@click.command()
@click.argument('coverage')
def main(coverage):
    data = read_coverage(coverage)
    for id in range(len(data)):
        parse_file_coverage(data[id])


def read_coverage(coverage):
    with open(coverage) as f:
        data = json.load(f)
    return data


def to_filename(url):
    path = urllib.parse.urlparse(url).path
    filename = os.path.basename(path)
    return filename


def parse_file_coverage(file_coverage):
    filename = to_filename(file_coverage['url'])
    if not filename:
        return
    ranges = file_coverage['ranges']
    text = file_coverage['text']

    print('Creating: {0}'.format(filename))

    output = open(filename, 'w')
    for range in ranges:
        output.write(text[range['start']:range['end']])
    output.close()


if __name__ == '__main__':
    main()
