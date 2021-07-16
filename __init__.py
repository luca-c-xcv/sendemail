from jinja2 import Environment, PackageLoader, select_autoescape, Template
from controller.powerfailure import powerfailure
from controller.sender import sender
import sys
import getopt

global configFile

def powerRestore():
    print( "restore" )

def powerFailure():
    print( "failure" )
    return
    pf = powerfailure() #create a powerfailure obj
    env = Environment( loader=PackageLoader('sendemail', 'templates'), autoescape=select_autoescape( ) ) #create env for template
    t = env.get_template( "template.html" ) #get email template
    template = t.render(TITLE=pf.getTitle(), pinto=pf.getIntro(), brief=pf.getBrief(), descr=pf.getDescr()) #template customisation
    mail = sender("Warning: power failure") #prepare to send email
    mail.send( template ) #send email with template




if __name__=='__main__':

    if( len( sys.argv ) < 2 ):
        print( "usage" )
        sys.exit(2)

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, ':frT', ["power-failure", "power-restore", "test"])
        print( opts )
    except getopt.GetoptError:
        print( "USAGE" )
        sys.exit(2)

    test = False
    pf = False
    pr = False
    for opt, args  in opts:
        if( opt in ('-T', '--test') ):
            test = True
        elif( opt in ('-f', '--power-failure' ) ):
            pf=True
        elif( opt in ( '-r', '--power-restore')  ):
            pr=True


    if( pr and pf ):
        print( 'Usage' )
        sys.exit(2)
    elif( test ):
        print("Insert testing config file path")
        file = input()

    if( pf ):
        powerFailure()
    elif( pr ):
        powerRestore()