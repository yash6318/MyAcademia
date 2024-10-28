# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class Applicants(models.Model):
#     applicantid = models.AutoField(db_column='ApplicantID', primary_key=True)  # Field name made lowercase.
#     firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', max_length=45)  # Field name made lowercase.
#     classtobeenrolled = models.IntegerField(db_column='ClassToBeEnrolled')  # Field name made lowercase.
#     lastschoolattended = models.CharField(db_column='LastSchoolAttended', max_length=100)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=1)  # Field name made lowercase.
#     dob = models.DateField(db_column='DOB')  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     bloodgrp = models.CharField(db_column='BloodGrp', max_length=4)  # Field name made lowercase.
#     aadhaarno = models.PositiveBigIntegerField(db_column='AadhaarNo', unique=True)  # Field name made lowercase.
#     contactno = models.BigIntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
#     father_s_name = models.CharField(db_column="Father's_Name", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     father_s_occupation = models.CharField(db_column="Father's_Occupation", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     father_s_aadhaarno = models.PositiveBigIntegerField(db_column="Father's_AadhaarNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     father_s_email = models.CharField(db_column="Father's_Email", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     father_s_contactno = models.BigIntegerField(db_column="Father's_ContactNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mother_s_name = models.CharField(db_column="Mother's_Name", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mother_s_occupation = models.CharField(db_column="Mother's_Occupation", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mother_s_aadhaarno = models.PositiveBigIntegerField(db_column="Mother's_AadhaarNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mother_s_email = models.CharField(db_column="Mother's_Email", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mother_s_contactno = models.BigIntegerField(db_column="Mother's_ContactNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     guardian_s_name = models.CharField(db_column="Guardian's_Name", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     guardian_s_occupation = models.CharField(db_column="Guardian's_Occupation", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     guardian_s_aadhaarno = models.PositiveBigIntegerField(db_column="Guardian's_AadhaarNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     guardian_s_email = models.CharField(db_column="Guardian's_Email", max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     guardian_s_contactno = models.BigIntegerField(db_column="Guardian's_ContactNo", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     familyincome = models.CharField(db_column='FamilyIncome', max_length=10)  # Field name made lowercase.
#     caste = models.CharField(db_column='Caste', max_length=5)  # Field name made lowercase.
#     religion = models.CharField(db_column='Religion', max_length=45)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'applicants'


# class ApplicationStatus(models.Model):
#     applicantid = models.OneToOneField(Applicants, models.DO_NOTHING, db_column='ApplicantID', primary_key=True)  # Field name made lowercase.
#     testscore = models.IntegerField(db_column='TestScore', blank=True, null=True)  # Field name made lowercase.
#     interviewerid = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='InterviewerID')  # Field name made lowercase.
#     classtobeenrolled = models.IntegerField(db_column='ClassToBeEnrolled')  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'application_status'


# class Attendance(models.Model):
#     enrollno = models.OneToOneField('Students', models.DO_NOTHING, db_column='EnrollNo', primary_key=True)  # Field name made lowercase.
#     class_field = models.IntegerField(db_column='Class')  # Field name made lowercase. Field renamed because it was a Python reserved word.
#     april = models.IntegerField(db_column='April', blank=True, null=True)  # Field name made lowercase.
#     may = models.IntegerField(db_column='May', blank=True, null=True)  # Field name made lowercase.
#     june = models.IntegerField(db_column='June', blank=True, null=True)  # Field name made lowercase.
#     july = models.IntegerField(db_column='July', blank=True, null=True)  # Field name made lowercase.
#     august = models.IntegerField(db_column='August', blank=True, null=True)  # Field name made lowercase.
#     september = models.IntegerField(db_column='September', blank=True, null=True)  # Field name made lowercase.
#     october = models.IntegerField(db_column='October', blank=True, null=True)  # Field name made lowercase.
#     november = models.IntegerField(db_column='November', blank=True, null=True)  # Field name made lowercase.
#     december = models.IntegerField(db_column='December', blank=True, null=True)  # Field name made lowercase.
#     january = models.IntegerField(db_column='January', blank=True, null=True)  # Field name made lowercase.
#     february = models.IntegerField(db_column='February', blank=True, null=True)  # Field name made lowercase.
#     march = models.IntegerField(db_column='March', blank=True, null=True)  # Field name made lowercase.
#     totalworking_days = models.IntegerField(db_column='TotalWorking_Days', blank=True, null=True)  # Field name made lowercase.
#     percentage = models.FloatField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'attendance'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class Classes(models.Model):
#     class_field = models.IntegerField(db_column='Class', primary_key=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
#     strength = models.IntegerField(db_column='Strength')  # Field name made lowercase.
#     classteacherid = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='ClassTeacherID')  # Field name made lowercase.
#     fees = models.IntegerField(db_column='Fees')  # Field name made lowercase.
#     subject1 = models.CharField(db_column='Subject1', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     maxmarksinsub1 = models.IntegerField(db_column='MaxMarksInSub1', blank=True, null=True)  # Field name made lowercase.
#     subject2 = models.CharField(db_column='Subject2', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     maxmarksinsub2 = models.IntegerField(db_column='MaxMarksInSub2', blank=True, null=True)  # Field name made lowercase.
#     subject3 = models.CharField(db_column='Subject3', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     maxmarksinsub3 = models.IntegerField(db_column='MaxMarksInSub3', blank=True, null=True)  # Field name made lowercase.
#     subject4 = models.CharField(db_column='Subject4', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     maxmarksinsub4 = models.IntegerField(db_column='MaxMarksInSub4', blank=True, null=True)  # Field name made lowercase.
#     subject5 = models.CharField(db_column='Subject5', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     maxmarksinsub5 = models.IntegerField(db_column='MaxMarksInSub5', blank=True, null=True)  # Field name made lowercase.
#     subject6 = models.CharField(db_column='Subject6', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     maxmarksinsub6 = models.IntegerField(db_column='MaxMarksInSub6', blank=True, null=True)  # Field name made lowercase.
#     subject7 = models.CharField(db_column='Subject7', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     maxmarksinsub7 = models.IntegerField(db_column='MaxMarksInSub7', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'classes'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class GuardianDetails(models.Model):
#     studentid = models.ForeignKey('Students', models.DO_NOTHING, db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
#     relationship = models.CharField(db_column='Relationship', max_length=45)  # Field name made lowercase.
#     contactno = models.BigIntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     occupation = models.CharField(db_column='Occupation', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     aadhaarno = models.PositiveBigIntegerField(db_column='AadhaarNo')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'guardian_details'


# class MainappUserProfiles(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     image = models.CharField(max_length=100)
#     user = models.OneToOneField(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'mainapp_user_profiles'


# class Results(models.Model):
#     enrollno = models.OneToOneField('Students', models.DO_NOTHING, db_column='EnrollNo', primary_key=True)  # Field name made lowercase.
#     class_field = models.IntegerField(db_column='Class')  # Field name made lowercase. Field renamed because it was a Python reserved word.
#     marksinsub1 = models.IntegerField(db_column='MarksInSub1', blank=True, null=True)  # Field name made lowercase.
#     marksinsub2 = models.IntegerField(db_column='MarksInSub2', blank=True, null=True)  # Field name made lowercase.
#     marksinsub3 = models.IntegerField(db_column='MarksInSub3', blank=True, null=True)  # Field name made lowercase.
#     marksinsub4 = models.IntegerField(db_column='MarksInSub4', blank=True, null=True)  # Field name made lowercase.
#     marksinsub5 = models.IntegerField(db_column='MarksInSub5', blank=True, null=True)  # Field name made lowercase.
#     marksinsub6 = models.IntegerField(db_column='MarksInSub6', blank=True, null=True)  # Field name made lowercase.
#     marksinsub7 = models.IntegerField(db_column='MarksInSub7', blank=True, null=True)  # Field name made lowercase.
#     percentagescore = models.FloatField(db_column='PercentageScore', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'results'


# class StudentDetails(models.Model):
#     enrollno = models.OneToOneField('Students', models.DO_NOTHING, db_column='EnrollNo', primary_key=True)  # Field name made lowercase.
#     aadhaarno = models.PositiveBigIntegerField(db_column='AadhaarNo', unique=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     contactno = models.BigIntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     dob = models.DateField(db_column='DOB')  # Field name made lowercase.
#     bloodgrp = models.CharField(db_column='BloodGrp', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     caste = models.CharField(db_column='Caste', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     religion = models.CharField(db_column='Religion', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     familyincome = models.CharField(db_column='FamilyIncome', max_length=10)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'student_details'


# class Students(models.Model):
#     enrollno = models.AutoField(db_column='EnrollNo', primary_key=True)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', max_length=45)  # Field name made lowercase.
#     class_field = models.IntegerField(db_column='Class')  # Field name made lowercase. Field renamed because it was a Python reserved word.
#     dateofenrollment = models.DateTimeField(db_column='DateOfEnrollment')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'students'


# class Subjects(models.Model):
#     subjectcode = models.CharField(db_column='SubjectCode', primary_key=True, max_length=10)  # Field name made lowercase.
#     subjectname = models.CharField(db_column='SubjectName', max_length=45)  # Field name made lowercase.
#     hod = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='HOD_ID')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'subjects'


# class TeacherDetails(models.Model):
#     teacherid = models.OneToOneField('Teachers', models.DO_NOTHING, db_column='TeacherID', primary_key=True)  # Field name made lowercase.
#     aadhaarno = models.PositiveBigIntegerField(db_column='AadhaarNo', unique=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     contactno = models.BigIntegerField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     dob = models.DateField(db_column='DOB')  # Field name made lowercase.
#     bloodgrp = models.CharField(db_column='BloodGrp', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     caste = models.CharField(db_column='Caste', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     religion = models.CharField(db_column='Religion', max_length=10, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'teacher_details'


# class Teachers(models.Model):
#     teacherid = models.IntegerField(db_column='TeacherID', primary_key=True)  # Field name made lowercase.
#     firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', max_length=45)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     teachessub = models.ForeignKey(Subjects, models.DO_NOTHING, db_column='TeachesSub')  # Field name made lowercase.
#     salary = models.BigIntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
#     dateofjoining = models.DateTimeField(db_column='DateOfJoining')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'teachers'
