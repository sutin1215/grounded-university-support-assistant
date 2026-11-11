# Pilot label review sheet (generated 11 Nov 2026)

The 90 labels still to confirm (all except the 6 you decided; the 5 truncated answers are included), grouped by question. Each answer shows the label, the deterministic checks
(gold numbers found; declined) and the LLM judge's label. Reply 'confirmed' or name any rows to change.
Source data: `eval/labels/pilot_label_evidence.csv`.


## Q01: What is the penalty if I submit my coursework late?

**Gold:** A 30% deduction from the mark, for work submitted up to 5 working days late.  
**Quote (ltbp-submission-coursework.pdf p1):** "30% deduction"

- **S1 = CORRECT** (numbers 5 30 of 5 30; declined no; judge CORRECT)  
  Coursework submitted up to five working days late receives a 30% deduction from the mark awarded.
- **S2 = WRONG** (numbers 5 of 5 30; declined no; judge WRONG) *Invents a 3% per day penalty; policy is a flat 30% deduction. States a 3%-per-day penalty; the policy is a flat 30% for up to 5 working days.*  
  For coursework submitted up to 5 working days after the deadline without approved mitigating circumstances, a penalty of 3% of the total available mark is deducted per working day. Any coursework submitted more than 5 working days late will automatically receive a mark of zero. If you have valid reasons for a late subm ...
- **S3 = CORRECT** (numbers 5 30 of 5 30; declined no; cites gold page yes; judge CORRECT)  
  If you submit your coursework late, there is a 30% mark deduction penalty for up to 5 working days [1]. Submitting after 5 working days results in a mark of 0F (fail) and no feedback [1]. However, if valid mitigating circumstances are approved, penalties may be waived or removed [2][3].

## Q02: If I hand in coursework 7 working days late, will it still be marked?

**Gold:** No. After 5 working days the mark is 0F (fail) with no feedback, unless mitigating circumstances are approved.  
**Quote (ltbp-submission-coursework.pdf p1):** "After 5 working days"

- **S1 = CORRECT** (numbers 0 of 0 5; declined no; judge CORRECT) *States 0F with no feedback for work over 5 days late, which answers the question.*  
  It is awarded 0 F with no feedback, unless mitigating circumstances are approved.
- **S2 = CORRECT** (numbers 5 of 0 5; declined no; judge CORRECT) *Says over 5 days late is not marked and gets zero; matches 0F in substance.*  
  Under Heriot-Watt University policy, coursework submitted more than 5 working days after the published deadline will not be marked and will automatically receive a mark of zero. Therefore, if you hand in your coursework 7 working days late, it will not be marked. If you experienced severe, unexpected circumstances that ...
- **S3 = CORRECT** (numbers 0 5 of 0 5; declined no; cites gold page yes; judge CORRECT)  
  If you submit coursework after 5 working days late, you will receive a mark of 0F (fail) and no feedback [1]. Therefore, if you submit coursework 7 working days late, it will not receive feedback and will be awarded a 0F grade unless mitigating circumstances are approved [1]. If mitigating circumstances are approved, l ...

## Q03: Can I ask my lecturer for an extension on an assignment?

**Gold:** No individual extensions. Exceptions: formally agreed reasonable adjustments, and class-wide extensions in exceptional circumstances.  
**Quote (ltbp-submission-coursework.pdf p1):** "No individual extensions"

- **S1 = ESCALATED** (declined yes; judge WRONG)  
  I can't answer that reliably. Please contact the relevant university office.
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT)  
  Under university policy, no individual extensions are allowed for coursework [2]. Class-wide extensions are permitted only in exceptional circumstances [1]. However, individual accommodations may apply where formally agreed as reasonable adjustments, or late submission penalties may be waived if valid mitigating circum ...

## Q04: Does the late penalty apply to class tests and presentations?

**Gold:** No. Online tests, presentations and other time-limited activities are excluded from the late submission rules.  
**Quote (ltbp-submission-coursework.pdf p1):** "Excluded assessments"

- **S1 = WRONG** (declined no; judge WRONG) *Matched the late-penalty FAQ; question is about tests and presentations.*  
  Coursework submitted up to five working days late receives a 30% deduction from the mark awarded.
- **S2 = CORRECT** (declined no; judge CORRECT)  
  No, the standard late submission penalties do not apply to class tests or presentations. Missing a scheduled test or presentation without prior authorization will generally result in a mark of zero. If you are unable to attend due to valid, unforeseen circumstances, you must submit a Mitigating Circumstances applicatio ...
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT)  
  No, late penalties do not apply to them, as presentations, online tests, and other time-limited activities are classified as excluded assessments [2].

## Q05: Can a course leader give the whole class more time for coursework?

**Gold:** Class-wide extensions are allowed only in exceptional circumstances.  
**Quote (ltbp-submission-coursework.pdf p1):** "Class-wide extensions"

- **S1 = ESCALATED** (declined yes; judge WRONG)  
  I can't answer that reliably. Please contact the relevant university office.
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT)  
  Class-wide extensions for coursework are allowed only in exceptional circumstances [2]. Otherwise, individual extensions are not permitted [1].

## Q06: How long do I have to send missing documents for a mitigating circumstances application?

**Gold:** Ten working days; otherwise the application is closed.  
**Quote (mc-procedure.pdf p2;3):** "ten working days"

- **S1 = WRONG** (numbers - of 10; declined no; judge WRONG) *Matched the evidence FAQ; does not give the 10-day limit.*  
  Evidence must be provided with the application, or a self-certification form for short periods. Applications without sufficient evidence are not accepted.
- **S2 = CORRECT** (numbers 10 of 10; declined no; judge CORRECT)  
  You must submit any missing supporting documents within **10 working days** of submitting your Mitigating Circumstances application. If you cannot obtain the required evidence within this timeframe due to delays beyond your control, you should notify the Student Hub or your School Office immediately. All supporting evi ...
- **S3 = CORRECT** (numbers 10 of 10; declined no; cites gold page yes; judge CORRECT)  
  You have ten working days to provide any requested missing documentation for a mitigating circumstances application [1][2]. If you do not provide the documentation within this timeframe, your application will expire and be marked as Closed [1][2].

## Q07: For how long can I self-certify mitigating circumstances?

**Gold:** The self-certified MC period must be no more than seven days.  
**Quote (mc-procedure.pdf p2):** "seven days"

- **S1 = CORRECT** (numbers 7 of 7; declined no; judge CORRECT)  
  Yes, for a period of no more than seven days, using the self-certification form.
- **S2 = WRONG** (numbers - of 7; declined no; judge WRONG) *Says 5 days; procedure says no more than seven days.*  
  At Heriot-Watt University, you can self-certify for mitigating circumstances for up to 5 consecutive calendar days without providing official evidence. If your circumstances affect you for longer than 5 days, you must submit independent supporting evidence, such as a medical certificate or doctor's note. Please ensure  ...
- **S3 = CORRECT** (numbers 7 of 7; declined no; cites gold page yes; judge CORRECT)  
  You can self-certify mitigating circumstances for a period of no more than seven days [1].

## Q08: What outcomes can a successful mitigating circumstances application lead to?

**Gold:** Mitigations include removing the late penalty, resit as same opportunity, disregarding a component, mapping a grade, or presenting to the progression/award board.  
**Quote (mc-procedure.pdf p4;7):** "late penalty"

- **S1 = WRONG** (declined no; judge WRONG) *Matched the evidence FAQ; question asks for outcomes.*  
  Evidence must be provided with the application, or a self-certification form for short periods. Applications without sufficient evidence are not accepted.
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT)  
  A successful mitigating circumstances application can result in various academic mitigations recommended by the Mitigating Circumstances Board [3]. Possible outcomes include removing a 30% late penalty on coursework, offering a resit as the same opportunity, or allowing dissertation submission at the next opportunity [ ...

## Q09: Will a mitigating circumstances claim be accepted without any evidence?

**Gold:** No. Applications with no or insufficient evidence are not accepted (a self-certification form may be used for short periods).  
**Quote (mc-procedure.pdf p2):** "sufficient evidence to support their application"

- **S1 = CORRECT** (declined no; judge CORRECT)  
  Evidence must be provided with the application, or a self-certification form for short periods. Applications without sufficient evidence are not accepted.
- **S2 = PARTIAL** (declined no; judge PARTIAL) *Core answer right but misses the self-certification route and adds invented evidence types. Borderline: says no, but claims independent evidence is always required and omits the self-certification route. PARTIAL (judge agrees).*  
  No, a mitigating circumstances claim will generally not be accepted without suitable supporting evidence. Heriot-Watt University requires independent, official documentation—such as a medical certificate or police report—to substantiate your claim. Submitting a claim without evidence will usually result in it being rej ...
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT) *Key facts right and cited; answer cut off mid-sentence by the output-token cap.*  
  A mitigating circumstances application will be marked as Not Accepted (Reject) if the student does not provide any or sufficient evidence to support it [1][3]. However, a student may submit a self-certification form if the mitigating circumstances period is for no more than seven days and a reason is provided for why e ...

## Q10: What grade do I need to pass a core course?

**Gold:** Grade D is the minimum to pass core courses.  
**Quote (hapsug.pdf p1):** "minimum requirement to pass core courses"

- **S1 = CORRECT** (declined no; judge CORRECT)  
  Grade D is the minimum to pass core courses.
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT)  
  A Grade D is the minimum requirement to pass core courses [1].

## Q11: What is the lowest grade that still gives me credit points?

**Gold:** Grade E is the minimum for gaining credit points.  
**Quote (hapsug.pdf p1):** "gaining credit points"

- **S1 = CORRECT** (declined no; judge CORRECT)  
  Grade E is the minimum grade for gaining credit points.
- **S2 = WRONG** (declined no; judge WRONG) *Says Grade D; document says Grade E is the minimum for credit.*  
  For undergraduate programmes at Heriot-Watt University Malaysia, the lowest grade that awards credit points is a **Grade D** (40%). For postgraduate programmes, the minimum passing grade required to earn credit points is typically a **Grade C** (50%). Any grades below these thresholds are considered fails and will not  ...
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT)  
  Grade E is the minimum requirement for gaining credit points for a course [1]. In contrast, Grade F does not carry any credits [2].

## Q12: How many times can I resit a course I failed?

**Gold:** One re-assessment opportunity per course, normally at the next diet (usually August).  
**Quote (hapsug.pdf p1):** "One re-assessment opportunity"

- **S1 = CORRECT** (numbers 1 of 1; declined no; judge CORRECT)  
  One re-assessment opportunity is permitted for each course, normally in August.
- **S2 = CORRECT** (numbers 1 of 1; declined no; judge CORRECT)  
  Under standard Heriot-Watt University regulations, you are normally permitted **one** resit (re-assessment) opportunity per failed course. If you do not pass the resit, you may be required to repeat the course in full in a subsequent semester, subject to your programme's progression rules. Please note that certain prof ...
- **S3 = CORRECT** (numbers 1 of 1; declined no; cites gold page yes; judge CORRECT)  
  One re-assessment opportunity is permitted for each course [2]. Re-assessments should usually be taken at the next available diet, which is typically in August [2]. If you need to defer a re-assessment until the next academic session, you must first seek permission from your School [2].

## Q13: Do I get any credits for an F grade?

**Gold:** No, Grade F does not carry any credits.  
**Quote (hapsug.pdf p1):** "does not carry any credits"

- **S1 = ESCALATED** (declined yes; judge WRONG)  
  I can't answer that reliably. Please contact the relevant university office.
- **S2 = CORRECT** (declined no; judge CORRECT)  
  No, you do not receive any credits for an F grade at Heriot-Watt University Malaysia. An F grade represents a fail, which means you have not met the required learning outcomes for the course. To earn the credits, you will need to successfully pass the course through reassessment or by retaking it. Please contact your A ...
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT)  
  No, a Grade F does not carry any credits [1].

## Q14: How much is the tuition fee per semester for international Computing Science students in 2026/27?

**Gold:** RM24,200 per semester (RM48,400 a year), plus 6% SST for non-Malaysian students (RM25,652 per semester including SST).  
**Quote (Fee-International.pdf p1):** "24,200.00"

- **S1 = ESCALATED** (numbers - of 6 24200 25652 48400; declined yes; judge WRONG)  
  I can't answer that reliably. Please contact the relevant university office.
- **S2 = ESCALATED** (numbers - of 6 24200 25652 48400; declined yes; judge WRONG) *Says it does not know the 2026/27 fee.*  
  I do not know the exact tuition fee per semester for international Computing Science students for the 2026/27 academic year, as official fee schedules for that period have not yet been published. Please check the Heriot-Watt University Malaysia website or contact the Admissions Office directly for the latest updates on ...
- **S3 = CORRECT** (numbers 6 24200 25652 of 6 24200 25652 48400; declined no; cites gold page yes; judge CORRECT) *Correct: RM24,200 per semester, RM25,652 with SST (checked against the PDF table). Per-semester fee and fee with SST right; annual total not asked.*  
  For international Computing Science students in 2026/27, the tuition fee per semester is RM 24,200.00 [1]. Including 6% SST, the total fee per semester is RM 25,652.00 [1].

## Q15: Do international students pay service tax on their fees?

**Gold:** Yes, a 6% service tax (SST) is charged to non-Malaysian students.  
**Quote (Fee-International.pdf p2;4):** "6% service tax"

- **S1 = WRONG** (numbers - of 6; declined no; judge WRONG) *Matched fee due-date FAQ instead of SST FAQ.*  
  Semester fees are payable in advance and must be fully paid before the semester starts.
- **S2 = WRONG** (numbers - of 6; declined no; judge WRONG) *Says tuition is exempt from SST; fee structure says 6% SST for non-Malaysian students.*  
  No, tuition fees for educational services at Heriot-Watt University Malaysia are exempt from Malaysian Service Tax (SST) for both local and international students. However, certain non-tuition administrative or ancillary charges may still be subject to prevailing government taxes. For a detailed breakdown of your speci ...
- **S3 = CORRECT** (numbers 6 of 6; declined no; cites gold page yes; judge CORRECT)  
  Yes, a 6% service tax (SST) will be charged to non-Malaysian students in accordance with expanded SST regulations effective 1 July 2025 [1][5]. The University also reserves the right to revise the total payable amount if there are future changes to the SST rate or the introduction of other taxes [1][5].

## Q16: How much is the registration fee for international students?

**Gold:** RM500 + 6% SST = RM530, non-refundable.  
**Quote (Fee-International.pdf p1;3):** "RM500"

- **S1 = WRONG** (numbers - of 6 500 530; declined no; judge WRONG) *Matched the payment-methods FAQ; no registration fee.*  
  Pay through the HWUM Online Payments page, by bank transfer or bankers' cheque, or at the Student Service Centre counter.
- **S2 = ESCALATED** (numbers - of 6 500 530; declined yes; judge WRONG) *Says it does not know the registration fee.*  
  I do not know the exact current registration fee as it varies depending on your programme level and required visa processing (EMGS) charges. Please check the official Heriot-Watt University Malaysia website
- **S3 = CORRECT** (numbers 6 500 530 of 6 500 530; declined no; cites gold page yes; judge CORRECT)  
  The non-refundable registration fee for international students is RM500 plus 6% SST, which totals RM530 [2].

## Q17: When do I have to pay my semester fees?

**Gold:** In advance: semester fees must be fully paid before the start of the semester.  
**Quote (Fee-International.pdf p2;4):** "payable in advance"

- **S1 = CORRECT** (declined no; judge CORRECT)  
  Semester fees are payable in advance and must be fully paid before the semester starts.
- **S2 = PARTIAL** (declined no; judge PARTIAL) *Vague; suggests payment may be due in week 1; document says fully in advance.*  
  Tuition fees are generally due by the payment deadline specified on your fee invoice, which is typically prior to the start of the semester or within the first week of classes. If you are paying via an approved installment plan, your payments must follow the dates outlined in your agreed payment schedule. You can view  ...
- **S3 = CORRECT** (declined no; cites gold page no; judge CORRECT) *Correct; cites the payment guide (also states fees are payable in advance), not the gold page. Payable in advance, right; cites a fees page other than the gold page.*  
  All fees are payable in advance [1]. Full settlement of your first semester fee is required upon registration or by the intake date [1]. Fees for subsequent semesters must be paid according to the due dates stated in the payment schedule or on your tuition fee invoice [1][4].

## Q18: Can I pay my tuition fees in instalments?

**Gold:** Yes, a 6-month instalment option with a Maybank credit card issued in Malaysia: 0% interest, minimum MYR 15,000, MYR 200 administration fee.  
**Quote (Fees-and-payment-guide-Malaysia.pdf p10):** "minimum amount to sign up"

- **S1 = WRONG** (numbers 6 of 0 6 200 15000; declined no; judge WRONG) *Matched SST FAQ instead of instalment FAQ.*  
  A 6% service tax is charged to non-Malaysian students.
- **S3 = CORRECT** (numbers 6 200 15000 of 0 6 200 15000; declined no; cites gold page no; judge CORRECT) *All conditions right ('interest-free' = 0%); cites a page other than the gold page.*  
  Yes, you may pay your tuition fee by instalment [1]. The university offers a 6-month instalment payment option using a Maybank credit card issued in Malaysia [1]. This plan is interest-free, requires a minimum charge of RM15,000, and includes a RM200 university administration fee [1]. You can apply for the instalment p ...

## Q19: How do I pay my fees online?

**Gold:** Through the HWUM Online Payments page ("Online Payments" tile in myHWU Apps or studentpayments.hw.ac.uk).  
**Quote (Fees-and-payment-guide-Malaysia.pdf p2;13):** "HWUM Online Payments"

- **S1 = WRONG** (declined no; judge WRONG) *Matched due-date FAQ instead of payment-methods FAQ.*  
  Semester fees are payable in advance and must be fully paid before the semester starts.
- **S3 = CORRECT** (declined no; cites gold page no; judge CORRECT)  
  Online payments via debit/credit card or direct bank transfer can be made through the Heriot-Watt Online Payment System on myHWU Apps or at https://studentpayments.hw.ac.uk [1]. To pay, you can select outstanding invoices or enter an amount for advanced payment before proceeding to pay [2]. When selecting your payment  ...

## Q20: Which email do I contact about fee payment receipts?

**Gold:** Send proof of payment to student-services-malaysia@hw.ac.uk.  
**Quote (Fees-and-payment-guide-Malaysia.pdf p2;18):** "student-services-malaysia@hw.ac.uk"

- **S1 = WRONG** (declined no; judge WRONG) *Matched payment-methods FAQ; no contact email.*  
  Pay through the HWUM Online Payments page, by bank transfer or bankers' cheque, or at the Student Service Centre counter.
- **S2 = WRONG** (declined no; judge WRONG) *Invents an email address (myfinance@hw.ac.uk).*  
  You can contact the Finance Office at Heriot-Watt University Malaysia by emailing **myfinance@hw.ac.uk** regarding your fee payment receipts. Please include your full name, Student ID number, and proof of payment in the email to help speed up the process.
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT) *Correct email, cited; also mentions emailing an Education Consultant, from passage [4].*  
  To request an official payment receipt, you should email the Student Service Centre (SSC) at student-services-malaysia@hw.ac.uk [1]. Additionally, when submitting a payment receipt, you should email it to your Education Consultant and HWUM@hw.ac.uk [4].

## U01: What time does the library close on Saturdays?

**Gold:** Not in the knowledge base: escalate.

- **S1 = DECLINED** (declined yes; judge DECLINED)  
  I can't answer that reliably. Please contact the relevant university office.
- **S2 = ANSWERED** (declined no; judge ANSWERED) *Invents library hours.*  
  During the semester, the Heriot-Watt University Malaysia Library closes at 6:00 PM on Saturdays (operating from 10:00 AM to 6:00 PM). Please note that opening hours may vary during semester breaks, exam periods, or public holidays.
- **S3 = DECLINED** (declined yes; judge DECLINED)  
  I can't find this in the official university documents I have. Please contact the relevant university office, for example Student Services, for help with this question.

## U02: Can I get a refund if I withdraw from my programme in Week 3?

**Gold:** Not covered by these documents: escalate.

- **S1 = DECLINED** (declined yes; judge DECLINED)  
  I can't answer that reliably. Please contact the relevant university office.
- **S2 = ANSWERED** (declined no; judge ANSWERED) *Invents a refund rule. Invents a refund rule; answer also cut off by the output-token cap.*  
  Under Heriot-Watt University Malaysia's policy, tuition fees are generally non-refundable if you withdraw after the second week of the semester. As you are withdrawing in Week 3, you
- **S3 = DECLINED** (declined yes; judge DECLINED)  
  I can't find this in the official university documents I have. Please contact the relevant university office, for example Student Services, for help with this question.

## U03: What is the charge if I pay my fees after the deadline?

**Gold:** Not covered by these documents: escalate.

- **S1 = ANSWERED** (declined no; judge ANSWERED) *Answers with the fee due date for a late-charge question.*  
  Semester fees are payable in advance and must be fully paid before the semester starts.
- **S2 = ANSWERED** (declined no; judge ANSWERED) *Invents an RM100 per month late fee.*  
  If you pay your tuition fees after the due date, a late payment fee of RM 100 per month will be charged to your student account. Additionally, overdue payments may result in administrative sanctions, such as the withholding of exam results or restriction of access to university facilities and portals. For specific inqu ...
- **S3 = DECLINED** (declined yes; judge DECLINED)  
  I can't find this in the official university documents I have. Please contact the relevant university office, for example Student Services, for help with this question.

## U04: How is my honours degree classification calculated?

**Gold:** Not covered by these documents: escalate.

- **S1 = DECLINED** (declined yes; judge DECLINED)  
  I can't answer that reliably. Please contact the relevant university office.
- **S2 = ANSWERED** (declined no; judge ANSWERED) *Gives generic UK classification bands not in the documents.*  
  Your honours degree classification is calculated based on the weighted average of your marks achieved in your upper stages of study (typically Stages 3 and 4). Generally, a First Class requires an average mark of 70% or above, an Upper Second (2:1) is 60–69%, a Lower Second (2:2) is 50–59%, and a Third Class is 40–49%. ...
- **S3 = DECLINED** (declined yes; judge DECLINED)  
  I can't find this in the official university documents I have. Please contact the relevant university office, for example Student Services, for help with this question.

## U05: Who is the programme leader for Computing Science?

**Gold:** Not in the knowledge base: escalate.

- **S1 = DECLINED** (declined yes; judge DECLINED)  
  I can't answer that reliably. Please contact the relevant university office.
- **S2 = DECLINED** (declined yes; judge DECLINED) *Says it does not know.*  
  I do not know the exact current programme leader for Computing Science at Heriot-Watt University Malaysia. Please check the official Heriot-Watt University Malaysia website or contact the School of Mathematical and Computer Sciences (MACS) administration office for the most up-to-date staff contact details.
- **S3 = DECLINED** (declined yes; judge DECLINED)  
  I can't find this in the official university documents I have. Please contact the relevant university office, for example Student Services, for help with this question.

## U06: What scholarships are available for Malaysian students?

**Gold:** Not in the knowledge base: escalate.

- **S1 = DECLINED** (declined yes; judge DECLINED)  
  I can't answer that reliably. Please contact the relevant university office.
- **S2 = ANSWERED** (declined no; judge ANSWERED) *Invents scholarship names.*  
  Heriot-Watt University Malaysia offers several scholarships for Malaysian students, including the High Achievers Scholarship for top performers in SPM, IGCSE, STPM, A-Levels, or Foundation studies. Eligible applicants can also apply for the Deputy Vice-Chancellor's Scholarship, Future Leaders Scholarship, and various f ...
- **S3 = DECLINED** (declined yes; judge DECLINED)  
  I can't find this in the official university documents I have. Please contact the relevant university office, for example Student Services, for help with this question.

## P01: Could my coursework be due on a Sunday?

**Gold:** Normally no: coursework deadlines should fall on weekdays, at equitable times for all time zones (e.g. 09:00-17:00 local time).  
**Quote (ltbp-submission-coursework.pdf p1):** "Coursework deadlines should fall on weekdays"

- **S1 = WRONG** (numbers - of 00 09 17; declined no; judge WRONG) *Returned the fee-payment FAQ; nothing about deadlines.*  
  Semester fees are payable in advance and must be fully paid before the semester starts.
- **S2 = PARTIAL** (numbers - of 00 09 17; declined no; judge PARTIAL) *Says deadlines are typically weekdays (right) but also that Sunday deadlines happen; the policy says deadlines should fall on weekdays.*  
  Standard Heriot-Watt University coursework deadlines are typically set on weekdays during working hours so that IT and academic support are available. However, certain online assessments or course leaders may occasionally set submission deadlines on weekends, including Sundays. You should always check your official cou ...
- **S3 = CORRECT** (numbers - of 00 09 17; declined no; cites gold page yes; judge CORRECT) *States weekdays and equitable times; cites the gold page.*  
  No, coursework deadlines should fall on weekdays and at equitable times for all time zones [1]. Therefore, your coursework should not be due on a Sunday [1].

## P02: Is my lecturer allowed to set a class test in the exam weeks?

**Gold:** No. Class tests must not be scheduled during exam periods.  
**Quote (ltbp-submission-coursework.pdf p1):** "Class tests must not be scheduled during exam periods"

- **S1 = WRONG** (declined no; judge WRONG) *Returned the extensions FAQ.*  
  No individual extensions are permitted. Students with reasonable adjustments should speak to the lecturer.
- **S2 = CORRECT** (declined no; judge CORRECT) *Says no class tests in exam weeks; extra advice is generic but not contradicting.*  
  No, lecturers are generally not permitted to schedule class tests during the official university examination weeks. Exam weeks are strictly reserved for centrally timetabled final examinations, while coursework and class tests should be completed during the regular teaching weeks. If a class test has been scheduled dur ...
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT) *Quotes the rule; cites the gold page.*  
  No, your lecturer is not allowed to set a class test during exam periods [1]. University policy explicitly states that class tests must not be scheduled during exam periods [1].

## P03: I got an E in a core course. Do I still need to retake it even though I got the credits?

**Gold:** Yes. Grade E gains the credit points, but a core or continuing course needs at least a Grade D to pass, so a re-assessment is required.  
**Quote (hapsug.pdf p1):** "you have to take a re-assessment because the course in question is a continuing or core course"

- **S1 = PARTIAL** (declined no; judge PARTIAL) *States D is the minimum for core courses but does not say a re-assessment is needed.*  
  Grade D is the minimum to pass core courses.
- **S2 = CORRECT** (declined no; judge CORRECT) *Key facts right (re-assessment needed, D needed for core); adds percentage bands not in the documents (check).*  
  Yes, you will generally need to retake or re-assess the course. In Heriot-Watt University's grading system, Grade E (30–39%) is a marginal fail, and core courses usually cannot be passed through compensation. You must achieve at least a Grade D (40%) in all core courses to fulfill your degree requirements. Please conta ...
- **S3 = CORRECT** (declined no; cites gold page yes; judge CORRECT) *Key facts right and cited; answer is cut off mid-sentence by the output-token cap.*  
  Yes, you will have to take a re-assessment because a core course requires a minimum of Grade D to pass [1]. Even though you have gained credit points with a Grade E, your

## P04: After I send in my MC form, how soon will I hear back?

**Gold:** Within ten working days of the university receiving the application and supporting evidence (outcome of the Stage 1 review).  
**Quote (mc-procedure.pdf p3):** "within ten working days from receipt of their application"

- **S1 = ESCALATED** (numbers - of 1 10; declined yes; judge WRONG) *Declined an answerable question.*  
  I can't answer that reliably. Please contact the relevant university office.
- **S2 = ESCALATED** (numbers - of 1 10; declined yes; judge WRONG) *Says it does not know the timeframe.*  
  I do not know the exact timeframe for receiving a response after submitting your MC form. Processing times may vary depending on whether your submission is for standard absence recording or a formal Mitigating Circumstances application. You can follow up directly with the Heriot-Watt University Malaysia Student Office  ...
- **S3 = CORRECT** (numbers 1 10 of 1 10; declined no; cites gold page no; judge CORRECT) *Ten working days; cites p2 and p6; p6 states the same fact (gold quote is on p3).*  
  The outcome of the initial review will be communicated to you within 10 working days of the university receiving your application and supporting evidence [1][4].

## N01: How much does it cost to resit a course I failed?

**Gold:** Not covered by these documents (they describe resits but give no resit fee): escalate.

- **S1 = DECLINED** (declined yes; judge DECLINED) *Escalated.*  
  I can't answer that reliably. Please contact the relevant university office.
- **S2 = DECLINED** (declined yes; judge DECLINED) *Says it does not know the cost; no amount invented.*  
  I do not know the exact current cost to resit a course, as fees depend on whether you are taking an assessment-only resit or retaking the entire module with tuition. Fees may also vary based on your specific program and
- **S3 = DECLINED** (declined yes; judge DECLINED) *NOT_FOUND, escalated.*  
  I can't find this in the official university documents I have. Please contact the relevant university office, for example Student Services, for help with this question.

## N02: How do I appeal against a decision on my mitigating circumstances?

**Gold:** Not covered by these documents (the MC procedure does not describe appeals): escalate.

- **S1 = ANSWERED** (declined no; judge ANSWERED) *Returned the MC evidence FAQ, which does not answer the appeal question.*  
  Evidence must be provided with the application, or a self-certification form for short periods. Applications without sufficient evidence are not accepted.
- **S2 = ANSWERED** (declined no; judge ANSWERED) *Invents an appeal process with a 10-working-day limit.*  
  To appeal a decision on your mitigating circumstances, you must submit a formal Academic Appeal within 10 working days of receiving your outcome. Your appeal must be based on valid grounds, such as procedural irregularity or new evidence that could not reasonably have been provided at the time of your original applicat ...
- **S3 = DECLINED** (declined yes; judge DECLINED) *NOT_FOUND, escalated.*  
  I can't find this in the official university documents I have. Please contact the relevant university office, for example Student Services, for help with this question.
