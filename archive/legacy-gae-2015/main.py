import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        title = "White Collar Boxing Training"
        subtitle = "World-class boxing training London"
        description = "White Collar Boxing Training offers premier world class training for professionals throughout London and the UK."
        keywords = "boxing training, white collar, collar boxing, advanced training,london,uk,training sessions,professionals,trainers"
        banner="<video style=\"width:100%;max-width: 100%;height:auto;z-index:-100;display: block;\" autoplay poster=\"/images/other/gary.png\"><source src=\"/videos/gary.ogv\" type=\"video/ogg\"><source src=\"/videos/gary.mp4\" type=\"video/mp4\"></video>"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("index.html")
        self.response.write(template.render(template_vars))

class StoryHandler(webapp2.RequestHandler):
    def get(self):
        title = "Our Story"
        subtitle = "Premier world-class boxing training in London"
        description = "We help professionals suit up and properly prepare for their big fight regardless of their current ability or skill set."
        keywords = "white collar,collar boxing,boxing training,training methods,boxer,big fight,training sessions,advanced boxing,advanced training"
        banner = "<picture><source srcset=\"/images/banner/banner.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner.jpg\" width=\"960\" height=\"378\" alt=\"White Collar Boxing Training\" /></picture>"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("story.html")
        self.response.write(template.render(template_vars))

class TrainersHandler(webapp2.RequestHandler):
    def get(self):
        title = "Trainers"
        subtitle = "We take pride in pushing our clients to their limits"
        description = "Over 20 years of experience with white collar boxing in London"
        keywords = "trainers,white collar,collar boxing,boxing training,gary foley,sean murphy,boxing training,boxer winning,our training"
        banner = "<picture><source srcset=\"/images/banner/banner_3.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner_3.jpg\" width=\"960\" height=\"378\" alt=\"White Collar Boxing Training\" /></picture>"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("trainers.html")
        self.response.write(template.render(template_vars))

class WhatsInvolvedHandler(webapp2.RequestHandler):
    def get(self):
        title = "Training"
        subtitle = "Offering a variety of boxing training levels"
        description = "Our trainers will help you understand the basics of white-collar boxing and guide you through each step one-on-one until you master each skill"
        keywords = "collar boxing,white collar,boxing training,training levels,skill set,intense training,london uk,beginner training,training advanced"
        banner = "<picture><source srcset=\"/images/banner/banner_2.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner_2.jpg\" width=\"960\" height=\"378\" alt=\"White Collar Boxing Training\" /></picture>"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("whats-involved.html")
        self.response.write(template.render(template_vars))

class ClassesHandler(webapp2.RequestHandler):
    def get(self):
        title = "Group and One-to-one classes"
        subtitle = "Offering a wide range of workshops for adults and children"
        description = "Following a well-structured conditioning program we will help you work on your fitness and your boxing techniques"
        keywords = "collar boxing,white collar,conditioning program,boxing training,boxing workshops,boxing and fitness programs,One-to-one lessons"
        banner = ""
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("classes.html")
        self.response.write(template.render(template_vars))

class GetInTouchHandler(webapp2.RequestHandler):
    def get(self):
        title = "Get in touch"
        subtitle = "Learn from the best white collar boxing trainers"
        description = "Our white collar boxing training is specifically tailored to help average business professionals unlock their physical and psychological strength."
        keywords = "collar boxing,white collar,our training,boxing trainers,training sessions,white collar boxing,get in touch,contact us today,boxing trainers"
        banner = "<picture><source srcset=\"/images/banner/banner_4.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner_4.jpg\" width=\"960\" height=\"378\" alt=\"White Collar Boxing Training\" /></picture>"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("get-in-touch.html")
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/story.html', StoryHandler),
    ('/trainers.html', TrainersHandler),
    ('/whats-involved.html', WhatsInvolvedHandler),
    ('/classes.html', ClassesHandler),
    ('/get-in-touch.html', GetInTouchHandler),
], debug=True)
