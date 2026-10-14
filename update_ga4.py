import os
import re

ga4_code = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-VGQGPDFB0C"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-VGQGPDFB0C');
</script>'''

files = ['index.html', 'factions.html', 'units.html', 'campaign.html', 'battles.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove existing GA4 if present
    pattern = r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-[^"]+"></script>\s*<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];\s*function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*gtag\(\'js\', new Date\(\)\);\s*gtag\(\'config\', \'G-[^\']+\'\);\s*</script>'
    content = re.sub(pattern, '', content)

    # Add GA4 after </style> tag
    if 'G-VGQGPDFB0C' not in content:
        content = content.replace('</style>', '</style>\n    ' + ga4_code)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Added GA4: {f}')

print('Done!')