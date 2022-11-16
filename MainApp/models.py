from django.db import models
from teacher.models import Teachers
from django.contrib.auth.models import User

# Create your models here.
class Applicants(models.Model):
    applicantid = models.AutoField(db_column='ApplicantID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45)  # Field name made lowercase.
    classtobeenrolled = models.IntegerField(db_column='ClassToBeEnrolled')  # Field name made lowercase.
    lastschoolattended = models.CharField(db_column='LastSchoolAttended', max_length=100)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bloodgrp = models.CharField(db_column='BloodGrp', max_length=4)  # Field name made lowercase.
    aadhaarno = models.PositiveBigIntegerField(db_column='AadhaarNo', unique=True)  # Field name made lowercase.
    contactno = models.BigIntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
    father_s_name = models.CharField(db_column="Father's_Name", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_occupation = models.CharField(db_column="Father's_Occupation", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_aadhaarno = models.PositiveBigIntegerField(db_column="Father's_AadhaarNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_email = models.CharField(db_column="Father's_Email", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_contactno = models.BigIntegerField(db_column="Father's_ContactNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_name = models.CharField(db_column="Mother's_Name", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_occupation = models.CharField(db_column="Mother's_Occupation", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_aadhaarno = models.PositiveBigIntegerField(db_column="Mother's_AadhaarNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_email = models.CharField(db_column="Mother's_Email", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_contactno = models.BigIntegerField(db_column="Mother's_ContactNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guardian_s_name = models.CharField(db_column="Guardian's_Name", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guardian_s_occupation = models.CharField(db_column="Guardian's_Occupation", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guardian_s_aadhaarno = models.PositiveBigIntegerField(db_column="Guardian's_AadhaarNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guardian_s_email = models.CharField(db_column="Guardian's_Email", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guardian_s_contactno = models.BigIntegerField(db_column="Guardian's_ContactNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    familyincome = models.CharField(db_column='FamilyIncome', max_length=10)  # Field name made lowercase.
    caste = models.CharField(db_column='Caste', max_length=5)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicants'

    def __str__(self):
        return self.firstname

class ApplicationStatus(models.Model):
    applicantid = models.OneToOneField(Applicants, models.DO_NOTHING, db_column='ApplicantID', primary_key=True)  # Field name made lowercase.
    testscore = models.IntegerField(db_column='TestScore', blank=True, null=True)  # Field name made lowercase.
    interviewerid = models.ForeignKey(Teachers, models.DO_NOTHING, db_column='InterviewerID')  # Field name made lowercase.
    classtobeenrolled = models.IntegerField(db_column='ClassToBeEnrolled')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'application_status'

class user_profiles(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='prof.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


