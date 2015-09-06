#!/bin/env python2
from multiprocessing import Pool, cpu_count
import click
import json
import requests

def load_from_file(src):
    """Load the file containing the list URLs into a list."""
    with open(src, 'r') as infile:
        return infile.read().splitlines()

def dump_to_file(dic, dest):
    """Dump the colletion of HTTP response times to a file in JSON."""
    with open(dest, 'w') as outfile:
        json.dump(dic, outfile, indent=4)

def time_http_response(url):
    """Measure the HTTP response time in miliseconds."""
    result = {}
    response = requests.get(url)
    response_time = '%02d' % (response.elapsed.total_seconds() * 1000)
    result['url'], result['response_time'] = url, response_time
    return result

@click.command()
@click.option('--infile', required = True, help = 'The path to the URL file.')
@click.option('--outfile', required = True, help = 'The path to the result file.')
def runner(infile, outfile):
    """This tool helps profiling HTTP response times for a list of URLs.
    It takes two arguments; an input file containing one URL per line.
    It will then dump the results in miliseconds as JSON to another file."""
    pool = Pool( processes=cpu_count() )
    dump_to_file(pool.map(time_http_response, load_from_file(infile)), outfile)
