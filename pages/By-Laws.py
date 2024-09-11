#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:17:03 2024

@author: aidenguenther
"""
import streamlit as st
from PIL import Image

##Header
image = Image.open('Logo2.png')
max_size = (200, 200)
image.thumbnail(max_size)

col1, col2, col3 = st.columns(3)

with col1:
    st.title("By-Laws", anchor=False)

with col3:
    st.image(image)

st.markdown('''
# Whitman Investment Company Bylaws

## I. Investment Strategy

### Investment Guidelines
The Whitman Investment Company—consisting of Members and Executive Officers—shall establish investment policies and procedures that govern the operations of the portfolio.
- These guidelines shall be adopted by at least a two-thirds (2/3) majority vote of the Membership.
- The policy shall outline:
  1. General objectives
  2. Focus sectors
  3. Methods of security analysis
  4. Guidelines for selling securities
  5. Benchmarks
  6. Asset allocation
  7. Risk assessment
  8. Exit strategy

Changes to the Investment Policy and Strategy shall be made as follows:
- Proposals must be disseminated to all members at least 24 hours before the meeting.
- A member of the Advisory Committee must be present for the vote, but they do not have voting power.
- Changes require a two-thirds (2/3) affirmative vote.

### Proposed Investments
- Any Member in good standing may propose an investment.
- Proposals must comply with our investment strategy and philosophy.
- Proposals are made using the following procedure:
  - Notify the CEO of the intent to research the investment.
  - Prepare a research report and submit it to the CEO no later than 48 hours before the meeting.
  - Present the proposal at the meeting, followed by a discussion and vote.

### Investment Votes
- All investment decisions must be presented to the general membership for a vote.
- The CEO has veto power but it can be overruled by a two-thirds majority vote.

### Investment Rules
- Initial purchases of an investment shall not exceed 7% of the portfolio's net asset value.
- If an investment increases to 15% of the portfolio's value, re-balancing is required.

### Review of Strategy
- The Board of Trustees shall review the Investment Policy and Strategy at least once a year, following the election of new Executive Officers.

## II. Membership

### Definition of Membership
- An attendee is anyone who attends a meeting but is not a Member, Trustee, or Executive Officer.
- A Member is granted membership after attending three consecutive general meetings and giving a presentation, followed by a majority vote.
- Trustees and Executive Officers are considered members with voting rights.

### Duties of Membership
- Members may vote in executive office elections and proposed investments.

### Retaining Membership
- Members must attend at least 2/3 of the previous semester's general meetings to retain their status.
- Exceptions are made for members studying abroad.

## III. Board of Trustees

### Definition of the Board of Trustees
- The Board is comprised of individuals who have demonstrated exceptional commitment to WIC.
- The Board may have a maximum of 8 members, not including current and past Executive Officers.

### Duties of the Board of Trustees
- Trustees have all duties of Membership.
- They must review presentations before they are presented to the general membership.

### Applying to be on the Board of Trustees
- An application includes a cover letter, a letter outlining reasons for selection, and a resume.
- The Executive Officers nominate applicants, and the Board fills vacant positions.

### Attendance for Board of Trustees
- Trustees must attend at least 2/3 of board meetings to retain their position.

### Removal from the Board of Trustees
- Trusteeship can be revoked by a two-thirds vote of the Executive Officers.

## IV. Executive Officers

### Duties of Executive Officers

#### CEO
- Determines the meeting schedule.
- Oversees all operations of WIC and ensures compliance with the constitution, bylaws, and investment strategy.

#### CFO
- Prepares quarterly and annual performance reports.
- Ensures investment theses comply with college guidelines.

#### COO
- Oversees educational programs, recruitment efforts, and outreach activities.

#### CIO
- Maintains all permanent records and prepares minutes for meetings.

### Attendance for Executive Officers
- Officers must attend all meetings; missing more than three meetings results in a performance review.

## V. Election Procedure

### Executive Qualifications
- Candidates must have completed 12 credits from Whitman College and be a Member of WIC.

### Election Process
- Elections are held before the last meeting of the fall semester.
- Officers hold office from January 1st to December 31st.

### Right to Petition
- Members may petition a recall of election votes if signed by at least 10% of the membership.

## VI. Impeachment and Removal

### Impeachment
- The Board of Trustees may initiate impeachment of any Officer, Trustee, or Member.
- A motion must be submitted in writing, and the accused has the right to defend themselves.

### Resignation
- Officers must provide a two-week notice to the Board of Trustees.

## VII. Meetings

### General Meetings
- Required attendance for Members, Trustees, and Executive Officers.

### Board Meetings
- Required attendance for Trustees and Executive Officers.

### Parliamentary Authority
- The Roberts Rules of Order newly revised edition is the authority.

## VIII. Advisory Committee

### Advisory Committee Composition
- Comprised of faculty members selected by the Department of Economics, the Dean of Faculty, and the College Treasurer.

### Advisory Committee Responsibilities
- Provides advice and instruction and can relieve WIC of management responsibilities if necessary.

## IX. Amendments

### Amendments to the By-Laws
- Proposals must be presented seven days prior to consideration.
- Amendments require a two-thirds (2/3) affirmative vote to pass.
''')
