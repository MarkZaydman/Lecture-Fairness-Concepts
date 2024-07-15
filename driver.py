
'''

driver.py

Mark A. Zaydman, MD, PhD
06/18/2024

Purpose: Driver for pdf presentation for fairness lecture

'''

#%% imports
# system
import datetime
import os

# third party
import weasyprint
from jinja2 import Environment, FileSystemLoader

# local
# import analytics

# %% helper functions

def main()->None:
    '''Generates automated report'''
    # This block defines the file and directory paths
    ROOT = os.getcwd() # replace with your own path
    ASSETS_DIR = os.path.join(ROOT,'assets')
    TEMPLAT_SRC = os.path.join(ROOT, 'templates')
    CSS_SRC = os.path.join(ROOT, 'static/css')
    DEST_DIR = os.path.join(ROOT, 'output')
    TEMPLATE = 'template.html'
    CSS = 'style.css'
    OUTPUT_FILENAME = f'Fairness_Concepts.pdf'  

    # make the output directory if it doesn't exist
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    # run analytics to generate display objects
    # analytics.main() # replace with call to your own analytics module
  
    # This block defines the variables to inject into the template
    ## You should customice this block to fit your own needs
    REPORT_TIME=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')   
    REPORT_MONTH=datetime.datetime.now().strftime('%Y-%m')   
    SOFTWARE_VERSION_HASH = f"{os.popen('git rev-parse HEAD').read().rstrip()}"
    SOFTWARE_VERSION_TAG = f"{os.popen('git describe --tags').read().rstrip()}"        
    template_vars = { 'assets_dir': 'file://' + ASSETS_DIR,
                     'report_month':REPORT_MONTH,
                     'report_time':REPORT_TIME,
                     'software_version_tag':SOFTWARE_VERSION_TAG,
                     'software_version_hash':SOFTWARE_VERSION_HASH}
    


    # this block generates the report    
    print('start generate report...')
    env = Environment(loader=FileSystemLoader(TEMPLAT_SRC))
    template = env.get_template(TEMPLATE)
    css = os.path.join(CSS_SRC, CSS)
    rendered_string = template.render(template_vars)
    html = weasyprint.HTML(string=rendered_string)
    report = os.path.join(DEST_DIR, OUTPUT_FILENAME)
    html.write_pdf(report, stylesheets=[css])
    print('file is generated successfully and under {}', DEST_DIR)


if __name__ == '__main__':
    main()
    
    
    # %%