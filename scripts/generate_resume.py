from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)


OUTPUT = "Karim_Ashraf_Product_Designer_Resume_2026.pdf"
INK = colors.HexColor("#132B47")
BLUE = colors.HexColor("#246FB4")
MUTED = colors.HexColor("#556274")
LINE = colors.HexColor("#CBD7E3")


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=24, leading=26, textColor=INK, spaceAfter=1))
styles.add(ParagraphStyle(name="ResumeTitle", parent=styles["Normal"], fontName="Helvetica", fontSize=11.6, leading=14, textColor=BLUE, spaceAfter=4))
styles.add(ParagraphStyle(name="Contact", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=11, textColor=MUTED, spaceAfter=4))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.6, leading=12.5, textColor=INK, spaceBefore=5, spaceAfter=2))
styles.add(ParagraphStyle(name="Body", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=11.1, textColor=colors.HexColor("#1C2735"), spaceAfter=2))
styles.add(ParagraphStyle(name="Skill", parent=styles["Normal"], fontName="Helvetica", fontSize=8.05, leading=10.3, textColor=colors.HexColor("#1C2735"), spaceAfter=1.2))
styles.add(ParagraphStyle(name="Role", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.35, leading=11, textColor=colors.HexColor("#202A36"), spaceAfter=0.5))
styles.add(ParagraphStyle(name="Company", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.2, leading=11.5, textColor=INK, spaceAfter=0.5))
styles.add(ParagraphStyle(name="Meta", parent=styles["Normal"], fontName="Helvetica", fontSize=8.1, leading=10, textColor=MUTED, alignment=TA_RIGHT, spaceAfter=1))
styles.add(ParagraphStyle(name="ResumeBullet", parent=styles["Body"], leftIndent=9, firstLineIndent=-7, bulletIndent=0, spaceAfter=1.5))
styles.add(ParagraphStyle(name="Small", parent=styles["Normal"], fontName="Helvetica", fontSize=7.8, leading=10, textColor=MUTED, spaceAfter=1))


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def section(title):
    return [p(title.upper(), "Section"), HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=0, spaceAfter=4)]


def role(company, title, dates, location, bullets):
    parts = [
        p(company, "Company"),
        p(f"<font color='#246FB4'><b>{title}</b></font> &nbsp;&nbsp; {dates} &nbsp;|&nbsp; {location}", "Small"),
    ]
    parts.extend(p(f"- {bullet}", "ResumeBullet") for bullet in bullets)
    parts.append(Spacer(1, 2.2))
    return KeepTogether(parts)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.45)
    canvas.line(16 * mm, 13 * mm, A4[0] - 16 * mm, 13 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(16 * mm, 8.5 * mm, "Karim Ashraf | Product Designer")
    canvas.drawRightString(A4[0] - 16 * mm, 8.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=16 * mm,
    leftMargin=16 * mm,
    topMargin=13 * mm,
    bottomMargin=18 * mm,
    title="Karim Ashraf - Product Designer Resume 2026",
    author="Karim Ashraf",
    subject="Product design, product strategy, growth, and AI-assisted delivery",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="resume")
doc.addPageTemplates(PageTemplate(id="resume", frames=[frame], onPage=footer))

story = [
    p("Karim Ashraf", "Name"),
    p("Product Designer | Product Strategy, Growth and AI-Assisted Delivery", "ResumeTitle"),
    p("Cairo, Egypt &nbsp;|&nbsp; (+20) 10 6915 3644 &nbsp;|&nbsp; karim.sn98@gmail.com &nbsp;|&nbsp; <link href='https://www.linkedin.com/in/karimashraf98/' color='#246FB4'>LinkedIn</link> &nbsp;|&nbsp; <link href='https://karimashraf666.github.io/' color='#246FB4'>Portfolio</link>", "Contact"),
    HRFlowable(width="100%", thickness=1.1, color=BLUE, spaceBefore=1, spaceAfter=5),
]
story += section("Profile")
story += [p("Product Designer with 4+ years of experience shaping and shipping consumer and B2B products across regulated services, SaaS, social commerce and AI-enabled ventures. Combines customer research, behavioral data, product strategy and technical understanding to turn complex problems into clear, usable experiences. Works across discovery, prioritization, prototyping, delivery and iteration, with a track record of improving conversion, supporting operational scale and aligning cross-functional teams.")]
story += section("Skills")
story += [
    p("<b>Product design:</b> Interaction design, journey design, responsive web and mobile, information architecture, prototyping, design systems, accessibility, implementation QA", "Skill"),
    p("<b>Discovery and growth:</b> Customer interviews, usability testing, funnel analysis, onboarding, activation, personalization, behavioral design, experimentation", "Skill"),
    p("<b>Product strategy and delivery:</b> Problem framing, MVP definition, prioritization, requirements, business-rule mapping, workshop facilitation, cross-functional delivery", "Skill"),
    p("<b>AI-assisted product building:</b> Research synthesis, rapid prototyping, specifications, edge-case exploration, backlog decomposition, agentic workflows, human validation", "Skill"),
    p("<b>Tools:</b> Figma, FigJam, Miro, Maze, Mixpanel, Notion, Google Workspace, ChatGPT", "Skill"),
]
story += section("Professional Experience")
story += [
    role("Money Fellows", "Product Designer - Full-time", "Feb 2025 - Present", "Cairo, Egypt - Hybrid", [
        "Led the Goals experience from discovery through rollout, reaching 12% organic engagement, 61.1% conversion to goal creation and 69.8% conversion into the circle-join flow.",
        "Contributed to Recommendation Engine phases 0-1, supporting 14% adoption, 6,000+ recommendation-driven bundles and approximately 48% conversion at high-performing new-user entry points.",
        "Improved onboarding using insights from 70+ customer interviews and behavioral analysis, reaching approximately 99% screen-to-screen conversion across the optimized sequence.",
        "Delivered a high-priority customer migration in under two weeks, aligning Product, Engineering, Risk, CRM/Marketing and Design across states, messaging, edge cases and handoff.",
        "Designed complex, trust-sensitive journeys involving eligibility, limits, verification, recommendations and lifecycle changes, translating business and technical rules into clear customer decisions.",
    ]),
    role("1MORETHING Ventures", "Product Designer - Part-time", "Mar 2024 - Feb 2025", "Remote", [
        "Turned ambiguous venture concepts into focused MVP scopes, end-to-end journeys, prototypes and decision-ready product direction.",
        "Shaped Layla HR, Inveasy, Daaj and JumlatyPro across AI HR automation, computer-vision stock counting, grocery assistance and B2B ordering.",
        "Mapped AI uncertainty, fallback behavior and human-review paths so technical limitations were visible in the customer experience.",
        "Connected user needs, business models and technical feasibility through flows, specifications, stakeholder reviews and delivery handoff.",
    ]),
]

story.append(PageBreak())
story += section("Professional Experience - Continued")
story += [
    role("Bluworks", "Product Designer - Full-time", "Dec 2023 - Jun 2024", "Cairo, Egypt - Hybrid", [
        "Designed a distinct fixed-tablet clock-in experience in response to client safety and operational concerns, helping reopen sales opportunities while preserving relevant app functionality.",
        "Designed configurable approval workflows and a dedicated managerial mode for different customer structures and workforce policies.",
        "Expanded payroll, attendance and bulk-upload capabilities, reducing repetitive customer-success work and improving platform scalability.",
        "Separated high-frequency frontline interactions from complex administrative workflows while keeping both contexts coherent within one product system.",
        "Worked with Product and Engineering from problem framing through implementation review, resolving states, permissions and operational edge cases.",
    ]),
    role("Sharwa", "Product Designer - Full-time", "Aug 2022 - Sep 2023", "Cairo, Egypt", [
        "Redesigned onboarding and purchase guidance using gamified progression, increasing app-open-to-order-placement conversion from 7% to 14%.",
        "Designed the Open Groups homepage experience, increasing group-joining conversion from 40% to 75% within two months.",
        "Planned and designed responsive mobile and web journeys that made group buying easier to understand, compare and complete.",
        "Facilitated alignment workshops across Product, Operations and Marketing, connecting customer behavior with delivery and commercial constraints.",
    ]),
]
story += section("Selected Product Initiative")
story += [
    role("Playful", "Founder, Product Designer and Product Owner", "2026", "Self-initiated", [
        "Directed AI collaborators to shape and build a live multi-product discovery platform with five public product doors and a shared district experience.",
        "Defined product boundaries, journeys, acceptance criteria and a domain-structured architecture spanning eight database schemas and a separate founder console.",
        "Used AI-assisted implementation to test product judgment in production while retaining human review, privacy boundaries and explicit beta limitations.",
    ])
]
story += section("Education and Credentials")
story += [
    p("<b>Mansoura University</b> | B.Sc. Communication and Information Engineering | Sep 2016 - Aug 2021 | A+ graduation project", "Body"),
    p("<b>DvCircles</b> | Business Scholarship | Mar 2020 - Jun 2020", "Body"),
    p("<b>Selected UXcel credentials:</b> UX Designer; Design and Product Leadership; Enhancing UX Workflow with AI; Service Design Fundamentals; Design Thinking for Product Teams; Workshop Facilitation", "Body"),
]
story += section("Leadership and Languages")
story += [p("<b>AIESEC, 2018-2021:</b> UI/UX Designer; Local Committee Vice President of B2C and Customer Experience; Organizing Committee President for Global Village. <b>Languages:</b> Arabic (native), English (professional).", "Body")]

doc.build(story)
