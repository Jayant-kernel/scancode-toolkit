from cluecode import copyrights

print("Testing copyright detection on scilab-Scilab file...")
result = list(copyrights.detect_copyrights(
    'tests/cluecode/data/copyrights/scilab-Scilab',
    include_copyrights=True,
    include_authors=False,
    include_holders=False
))

print(f'Total copyrights found: {len(result)}')
print()

inria_results = [c for c in result if 'INRIA' in c.copyright or 'Scilab' in c.copyright or 'ENPC' in c.copyright]
print(f'INRIA/Scilab/ENPC related copyrights: {len(inria_results)}')
print()

for c in inria_results:
    print(f'Line {c.start_line}: {c.copyright}')
