from jinja2 import Environment, PackageLoader, select_autoescape, Template, FileSystemLoader
from controller.powerfailure import powerfailure
from controller.powerrestore import powerrestore
from controller.powerkill import powerkill
from controller.sender import sender
import sys
import getopt
import os

app = sys.modules['__main__']
DIRPATH = os.path.dirname( app.__file__ )


def powerRestore( test ):
    pr = powerrestore()  # create a powerrestore obj
    env = Environment(loader=FileSystemLoader(DIRPATH + '/templates'), autoescape=select_autoescape())  # create env for template
    t = env.get_template("template.html")  # get email template
    template = t.render(TITLE=pr.getTitle(), pinto=pr.getIntro(), brief=pr.getBrief(), timeDescr=pr.getTimeDescr(), percento=pr.getPercDescr(), pf=False, pr=True)  # template customisation
    mail = sender( test, "Warning: power is back" )  # prepare to send email
    mail.send(template)  # send email with template

def powerFailure( test ):
    pf = powerfailure() #create a powerfailure obj
    env = Environment( loader=FileSystemLoader(DIRPATH + '/templates'), autoescape=select_autoescape( ) ) #create env for template
    t = env.get_template( "template.html" ) #get email template
    template = t.render(TITLE=pf.getTitle(), pinto=pf.getIntro(), brief=pf.getBrief(), timeDescr=pf.getTimeDescr(), percento=pf.getPercDescr(), pf=True, pr=False ) #template customisation
    mail = sender( test, "Warning: power failure" ) #prepare to send email
    mail.send( template ) #send email with template

def powerKill( test ):
    pk = powerkill()
    env = Environment( loader=FileSystemLoader(DIRPATH + '/templates' ), autoescape=select_autoescape( ) )
    t = env.get_template( "template.html" )
    template = t.render(TITLE=pk.getTitle(), pintro=pk.getIntro(), breif=pk.getBrief(), pf=False, pr=False, pk=True )
    mail = sender( test, "Warning: kill server" )
    # mail.send( template )
    file = open( 'test.html', "w" )
    file.write( template )
    file.close()


if __name__=='__main__':

    if( len( sys.argv ) < 2 ):
        print( "usage" )
        sys.exit(2)

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, ':frkT', ["power-failure", "power-restore", "power-kill", "test"])
    except getopt.GetoptError:
        print( "USAGE" )
        sys.exit(2)

    test = False
    pf = False
    pr = False
    pk = False
    for opt, args  in opts:
        if( opt in ('-T', '--test') ):
            test = True
        elif( opt in ('-f', '--power-failure' ) ):
            pf=True
        elif( opt in ( '-r', '--power-restore')  ):
            pr=True
        elif( opt in ( '-k', '--power-kill')  ):
            pk=True


    if( pr and pf and pk ):
        print( 'Usage' )
        sys.exit(2)

    if( pf ):
        powerFailure( test )
    elif( pr ):
        powerRestore( test )
    elif( pk ):
        powerKill( test )