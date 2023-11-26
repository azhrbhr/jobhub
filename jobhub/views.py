from django.views.generic import TemplateView
from django.contrib.auth.models import User
from jobs.models import Job, Company


class HomePageView(TemplateView):
    template_name = "home/home.html"

    # def create_dummy_jobs():
    #     # Create or retrieve companies
    #     facebook, created = Company.objects.get_or_create(name='Facebook')
    #     google, created = Company.objects.get_or_create(name='Google')
    #     twitter, created = Company.objects.get_or_create(name='Twitter')

    #     Job.objects.create(
    #         poster=User.objects.first(),
    #         title='Software Engineer',
    #         company=facebook,
    #         description='Join our team as a Software Engineer and work on cutting-edge projects.',
    #         location='Menlo Park, CA'
    #     )

    #     Job.objects.create(
    #         poster=User.objects.first(),
    #         title='Product Manager',
    #         company=facebook,
    #         description='We are looking for an experienced Product Manager to lead innovative initiatives.',
    #         location='Menlo Park, CA'
    #     )

    #     Job.objects.create(
    #         poster=User.objects.first(),
    #         title='Data Analyst',
    #         company=facebook,
    #         description='Analyze and interpret data to help drive key business decisions.',
    #         location='Menlo Park, CA'
    #     )

    #     # Dummy jobs for Google
    #     Job.objects.create(
    #         poster=User.objects.first(),
    #         title='Machine Learning Engineer',
    #         company=google,
    #         description='Explore the frontier of machine learning as a key member of our research team.',
    #         location='Mountain View, CA'
    #     )

    #     Job.objects.create(
    #         poster=User.objects.first(),
    #         title='UX Designer',
    #         company=google,
    #         description='Shape the user experience for our products and collaborate with cross-functional teams.',
    #         location='Mountain View, CA'
    #     )

    #     Job.objects.create(
    #         poster=User.objects.first(),
    #         title='Software Development Manager',
    #         company=google,
    #         description='Lead and manage a team of software developers in delivering high-quality software products.',
    #         location='Mountain View, CA'
    #     )

    #     # Dummy jobs for Twitter
    #     Job.objects.create(
    #         poster=User.objects.first(),
    #         title='Data Scientist',
    #         company=twitter,
    #         description='Turn data into insights and drive strategic decisions as a Data Scientist at Twitter.',
    #         location='San Francisco, CA'
    #     )

    #     Job.objects.create(
    #         poster=User.objects.first(),
    #         title='Security Engineer',
    #         company=twitter,
    #         description='Enhance the security posture of our platform by joining our dedicated security team.',
    #         location='San Francisco, CA'
    #     )

    #     Job.objects.create(
    #         poster=User.objects.first(),
    #         title='Product Designer',
    #         company=twitter,
    #         description='Design and prototype innovative features for our products.',
    #         location='San Francisco, CA'
    #     )

    # create_dummy_jobs()
