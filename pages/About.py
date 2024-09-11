#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:19:21 2024

@author: aidenguenther
"""

import streamlit as st
from PIL import Image
from st_social_media_links import SocialMediaIcons

##Header
image = Image.open('Logo2.png')
max_size = (200, 200)
image.thumbnail(max_size)

col1, col2, col3 = st.columns(3)

with col1:
    st.title("About", anchor=False)

with col3:
    st.image(image)


st.markdown("""
## The Whitman Investment Company (WIC)

The Whitman Investment Company (WIC) was originally founded in the spring of 1998 as the Whitman Money-Makers Society. The Whitman Money-Makers was a forum where Whitman Students interested in investing could gather to share stock tips as well as share knowledge. In 1999, the group evolved from that organization to the Whitman Investment Company. With the new name, the Company also adopted its new focus as an educational organization. While relying on the knowledge of Company Trustees, Whitman College Economics Faculty (Pete Parcells), and Whitman Financial Staff for initial informational input, the WIC now focuses on the education and training of students.

> “The primary function of the Whitman Investment Company is to serve as an extension of the course offerings at Whitman College. The College is dedicated to learning, scholarship, personal growth, education of character, and personal responsibility.” Based upon those ideals, the Whitman Investment Company defines its mission: to apply the foundations gained in a liberal arts education to the practical world of finance while providing investment returns to the Whitman College community.

The transition to an educational organization was achieved by the WIC trustees in conjunction with the support of the Economics Department and Whitman College. A change in the use of the William M. Allen Endowment allowed the WIC to initiate fulfillment of its stated mission. The WIC would now provide practical education through the management of a real money portfolio of securities. This educational experience would enhance what was taught in courses at Whitman College. 

Beginning in the spring of 2001, this was accomplished by the Whitman Investment Company’s acceptance of both assets and management responsibility of the William M. Allen – Boeing Student Investment Fund. Money for the Fund comes from the William M. Allen – Boeing Lectureship and Student Investment Endowment. The purpose of the Fund is to enhance students’ interest in equity and fixed income investments and in the basic techniques of wise investing through practical experience. The purpose is also to provide an understanding of and learning opportunities in the field of business investment, economics, and management. Lastly, the Fund provided for the education of students through various activities and events. These events have included campus visits of individuals distinguished in industry, finance, technology, and manufacturing. These visits, lectures, and forums have provided students and gatherings of the larger community with practical knowledge of the business and financial world.

WIC student trustees have attended professional seminars (see the WIC at the WAC), professional meetings (AAWE financial sessions), and various training and educational events (e.g., educational tours of the Boeing manufacturing facilities, and Saltchuk facilities in Seattle).

**William M. Allen** was the President of the Boeing Company from 1945 to 1968. A lawyer whose background was not in engineering or business, Allen demonstrated extraordinary business vision and leadership and is a part of our nation’s aviation history. Allen was one of the key people who helped Boeing become a world leader in commercial aviation. Allen’s daughter Nancy, Whitman Class of 56, and her husband Grant Silvernale, Whitman Class of 50, established the William M. Allen Endowment in 1979 and arranged in the fall of 2000 to move the fund to the Whitman Economics Department for the use of the Fund in its present form.

At its inception, the Fund pursued an aggressive growth strategy primarily in the securities of companies with innovating products or positions of substantial leadership in technological sectors such as biotechnology, telecommunications, or the Internet. As the WIC matured and with the volatility in the market, the WIC shifted to a more diversified strategy with a core portfolio of long-term growth prospects and a portion of the funds devoted to aggressive growth. This modified portfolio approach has led to successful returns on the WIC investment funds.

The Whitman Investment Company is a successful extension of the Whitman College education. Students of all disciplines have become trustees in the WIC and in conjunction with other student participants, Whitman staff, and Whitman Economics Department advisors; all participants have become better educated and have experientially participated in the world of investment and finance.
""")


social_media_links = [
    "https://www.instagram.com/whitmaninvestmentcompany/",
    "https://www.linkedin.com/company/whitman-wic",
]

social_media_icons = SocialMediaIcons(social_media_links)

social_media_icons.render()