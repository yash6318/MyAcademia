# from django.db import models
# # Create your models here.

# class Subjects(models.Model):
#     subjectcode = models.CharField(db_column='SubjectCode', primary_key=True, max_length=10)  # Field name made lowercase.
#     subjectname = models.CharField(db_column='SubjectName', max_length=45)  # Field name made lowercase.
#     hod = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='HOD_ID')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'subjects'

#     def __str___(self):
#         return self.subjectcode


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

#     def __str___(self):
#         return self.firstname

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

#     def __str__(self):
#         return self.firstname

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
