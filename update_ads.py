import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/8117d0aa8b2f6f5eb61b58e95b1cebae"></script>
<script data-cfasync="false" src="https://bauval.org/14/924bdc44d5311a6de98b844aeb559079"></script>
<script>
  atOptions = {
    'key' : 'ce9ae992879a19ec8755b12ab72a7d38',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/ce9ae992879a19ec8755b12ab72a7d38"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-8117d0aa8b2f6f5eb61b58e95b1cebae"></div>
</div>'''

files = ['index.html', 'factions.html', 'units.html', 'campaign.html', 'battles.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if 'ce9ae992879a19ec8755b12ab72a7d38' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-8117d0aa8b2f6f5eb61b58e95b1cebae' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')