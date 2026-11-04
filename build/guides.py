# PlainWarden how-to guides. Executed by build_site.py after page(); writes public/guides/*.html.
# Content is general guidance, reviewed 2026-10-30. Keep regulatory references exact; no vendor endorsements.
import os, html as _h
GUIDES_REVIEWED = 'October 30, 2026'
os.makedirs(OUT + '/guides', exist_ok=True)

def _ol(items): return '<ol>' + ''.join('<li>' + i + '</li>' for i in items) + '</ol>'
def _ul(items): return '<ul>' + ''.join('<li>' + i + '</li>' for i in items) + '</ul>'

G = []  # (slug, title, summary, why, steps, done, refs)

G.append(('two-step-login', 'Turn on two-step login',
 'Require a second step, such as an authenticator app code, whenever anyone signs in to a system that holds client information.',
 'A stolen password is the most common way into a small firm. Two-step login (multi-factor authentication) blocks most of those attempts, because the attacker also needs your phone or security key. The FTC Safeguards Rule requires it for anyone accessing any information system that holds customer information, unless your Qualified Individual approves an equivalent control in writing.',
 ['List every system that holds client information: tax software, email, cloud storage, client portal, bookkeeping software, password manager, remote access and IRS e-Services.',
  'For each one, open the security or sign-in settings and turn on two-step login for every user, not just yourself. In business email (Microsoft 365, Google Workspace), the administrator can require it for all accounts.',
  'Use an authenticator app or a hardware security key where offered. Text-message codes are better than nothing, but easier to intercept.',
  'Save each account\'s backup codes somewhere safe, such as your password manager or a locked drawer, so a lost phone doesn\'t lock you out.',
  'If a system can\'t support two-step login, the FTC Safeguards Rule allows a reasonably equivalent or more secure control only if your Qualified Individual approves it in writing. A strong password alone is not equivalent. Record the control and the written approval, and plan to move off that system.',
  'Check again whenever you add a system or a person.'],
 ['Every system on your list shows two-step login on for every user.', 'Any exception is written down and approved by the Coordinator.'],
 ['16 CFR 314.4(c)(5)', 'IRS Publication 4557']))

G.append(('encryption', 'Encrypt computers, phones and drives',
 'Turn on the built-in encryption on every device that stores client information, so a lost or stolen device doesn\'t expose it.',
 'A lost laptop with an unencrypted drive is a reportable breach in many states. With encryption on and a strong sign-in, the data is unreadable without the password. The FTC Safeguards Rule requires encryption of customer information at rest and in transit, or an alternative control approved by your Qualified Individual.',
 ['<b>Windows:</b> turn on BitLocker (Windows Pro and Business editions), or Device encryption on supported Home devices (Settings → Privacy &amp; security → Device encryption). Save the recovery key to your business account or print it and lock it up.',
  '<b>Mac:</b> turn on FileVault under System Settings → Privacy &amp; Security, and store the recovery key safely.',
  '<b>Phones and tablets:</b> iPhones, iPads and current Android devices encrypt automatically once a passcode is set. Require a passcode of at least six digits and auto-lock after a few minutes.',
  '<b>USB and external drives:</b> use BitLocker To Go, an encrypted drive, or stop using removable drives for client data.',
  '<b>Servers and network storage (NAS):</b> turn on volume or folder encryption in the device settings, and make sure backups of it are encrypted too.',
  'Record each device and its encryption status in your inventory (Attachment E of your plan).'],
 ['Every device in your inventory shows encryption on.', 'Recovery keys are stored where the Coordinator can reach them.'],
 ['16 CFR 314.4(c)(3)', 'IRS Publication 4557']))

G.append(('backups', 'Back up client data and test a restore',
 'Keep current, encrypted copies of client data somewhere separate from your computers, and prove you can restore them.',
 'Ransomware and hardware failure are survivable if you have a backup that the attacker can\'t reach and you know it works. A backup you\'ve never restored from is a guess.',
 ['Decide what must be backed up: tax software data, client documents, email and bookkeeping files.',
  'Follow the 3-2-1 idea: three copies of your data, on two different kinds of storage, with one copy off-site or in a cloud backup service.',
  'Turn on encryption for the backup, and use two-step login on the backup service account.',
  'Keep at least one copy that ordinary computers can\'t change or delete (an immutable or versioned cloud backup, or a drive you disconnect).',
  'Restore a test folder to a separate location at least once a year, and after any change to how you back up. Open a few files to confirm they work.',
  'Write down the date of the test and what you restored.'],
 ['Backups run automatically and are encrypted.', 'A restore test in the past 12 months is recorded.'],
 ['IRS Publication 4557', '16 CFR 314.4(c)(3)']))

G.append(('secure-file-exchange', 'Exchange documents securely',
 'Send and receive client documents through a secure portal or encrypted email, never as ordinary email attachments or texts.',
 'Ordinary email can be intercepted, forwarded or sit unprotected in a mailbox for years. The FTC Safeguards Rule requires customer information to be encrypted in transit.',
 ['Pick one or two approved channels: a client portal from your tax software or document provider, or encrypted email (for example, Microsoft 365 message encryption or a secure email service).',
  'Turn on two-step login for the portal and for staff accounts on it.',
  'Tell clients how to send you documents, and include the instructions in your engagement letter.',
  'If a client emails an SSN or tax document, move it into your secure system, delete the email from your mailbox, and remind the client of the secure option.',
  'Never send passwords for encrypted files in the same message as the file. Share them by phone or text.',
  'Confirm unexpected requests to send information or change payment details by calling a number you already have.'],
 ['Staff know the approved channels and use them.', 'Your engagement letter or client instructions name the approved channel.'],
 ['16 CFR 314.4(c)(3)', 'IRS Publication 4557']))

G.append(('sign-in-alerts', 'Turn on sign-in alerts and activity logs',
 'Keep a record of who signs in and what they do, get alerts for unusual sign-ins, and have someone review them.',
 'Logs are how you find out a password was stolen before it becomes a breach. The FTC Safeguards Rule requires firms to monitor and log authorized users\' activity and detect unauthorized access.',
 ['In business email, turn on the audit log (Microsoft 365: Microsoft Purview audit; Google Workspace: Admin console reports) and alerts for suspicious sign-ins and new forwarding rules.',
  'In your tax software and cloud storage, turn on sign-in notifications and activity history where available.',
  'Turn on new-device or new-location sign-in emails for every account that offers them.',
  'Name one person to review alerts, and a backup. Check alerts the day they arrive and skim activity logs at least monthly.',
  'If you see a sign-in you can\'t explain, change that password, sign out all sessions, and tell the Coordinator.'],
 ['Activity records and alerts are on for email and tax software.', 'A named person reviews them, and reviews are noted.'],
 ['16 CFR 314.4(c)(8)', 'IRS Publication 4557']))

G.append(('passwords', 'Use a password manager and unique passwords',
 'Give every account its own long password, stored in a business password manager.',
 'When one site is breached, attackers try the same password everywhere else. Unique passwords stop that. Current NIST guidance favors long passwords and checking against known-breached passwords over forced periodic changes.',
 ['Choose a business password manager with two-step login and shared vaults for the firm.',
  'Have each person create a long master password (a passphrase of four or more random words works well) and turn on two-step login for it.',
  'Move every work password into the manager and replace reused or short ones with generated passwords.',
  'Share firm accounts through the manager\'s shared vault, not by email or sticky note. Better still, give each person their own login.',
  'Change a password right away if it may have been exposed. You don\'t need to change strong, unique passwords on a schedule.',
  'When someone leaves, remove them from the password manager and change any shared passwords they knew.'],
 ['Everyone uses the password manager.', 'No password is reused across work accounts.'],
 ['NIST SP 800-63B', 'IRS Publication 4557']))

G.append(('retention-disposal', 'Set retention periods and dispose of records',
 'Decide how long you keep each kind of record, lock up what you keep, and securely destroy what you don\'t need.',
 'Data you no longer hold can\'t be stolen. The FTC Safeguards Rule requires disposing of customer information no later than two years after it was last used to serve the customer, unless you need it for business, the law requires keeping it, or targeted disposal isn\'t feasible. Other rules set minimums: for example, paid preparers keep a copy or list of returns they prepared for at least three years.',
 ['List what you keep: returns, source documents and workpapers, signature forms such as Form 8879, engagement letters, and records of former clients.',
  'Set a retention period for each, checking IRS, state and professional requirements with your adviser. Write it into your plan.',
  'Keep paper records in locked cabinets or a locked room, with off-site storage that is locked and access-restricted.',
  'Shred paper with a cross-cut shredder or a shredding service that gives you a certificate of destruction.',
  'Before disposing of computers, phones, drives or copiers with hard drives, wipe them with a method that meets NIST SP 800-88, or have them physically destroyed and get a certificate.',
  'Once a year, find and dispose of records past their retention period.'],
 ['Retention periods are written down.', 'A yearly disposal is done and recorded, with certificates where a vendor did the work.'],
 ['16 CFR 314.4(c)(6)', 'IRC §6107(b)', 'NIST SP 800-88']))

G.append(('vendor-security', 'Check a vendor\'s security',
 'Choose providers that can protect client information, require it in writing, and review them each year.',
 'Your tax software, email, cloud storage and IT provider hold or can reach your client data. The FTC Safeguards Rule requires firms to select capable providers, require safeguards by contract, and periodically assess them.',
 ['Keep a list of every provider that can access client information (the Vendors page in your portal does this).',
  'Before you sign up, ask how they protect data: encryption, two-step login, breach notification and, for larger providers, a security report such as SOC 2.',
  'Check the contract or terms of service for a commitment to protect your information and tell you about a breach. If it\'s missing, ask for a data protection addendum.',
  'Turn on two-step login on your account with each provider and limit who at your firm has access.',
  'Once a year, confirm each provider still meets these points and you still need them. Record the date.',
  'When you stop using a provider, export what you need and have them delete the rest.'],
 ['Every provider on your list has a review date in the past year.', 'Contracts with providers that hold client data include security terms.'],
 ['16 CFR 314.4(f)']))

G.append(('section-7216', 'Tax return information and client consent',
 'Use tax return information only to prepare returns unless the client has given consent in the form the IRS requires.',
 'Internal Revenue Code §7216 restricts how preparers use and disclose tax return information. Uses beyond preparing the return, such as marketing other services, generally need the taxpayer\'s written consent in a specific format. This guide is an overview only; confirm your situation with your adviser.',
 ['List every way your firm uses client tax information besides preparing and filing returns: marketing other services, sharing with affiliated businesses, outsourcing, or entering it into software or AI tools.',
  'For each use, check with your adviser whether consent is needed and whether an exception applies.',
  'Where consent is needed, use consent language that meets Treasury Regulation §301.7216-3 and Revenue Procedure 2013-14, and get it signed before the use or disclosure.',
  'If any return work or information goes to a preparer or service outside the United States, ask your adviser about the additional consent rules that apply.',
  'Keep signed consents with the client file for your retention period.',
  'Train staff that client tax information isn\'t used for anything else without checking first.'],
 ['Every use beyond preparing returns is either covered by signed consent or confirmed by your adviser as not needing it.'],
 ['IRC §7216', 'Treas. Reg. §301.7216-3', 'Rev. Proc. 2013-14']))

G.append(('updates-antimalware', 'Keep computers updated and protected',
 'Run supported systems with automatic updates and security software, and use non-administrator accounts for everyday work.',
 'Most malware relies on known, already-fixed weaknesses or on a user account that can install anything. Updates and limited accounts close both doors.',
 ['Replace any computer running an operating system that no longer gets security updates.',
  'Turn on automatic updates for the operating system, browsers, tax software and other apps.',
  'Use built-in security (Microsoft Defender on Windows, XProtect on Mac) or a business security product, kept on and current.',
  'Give each person a standard (non-administrator) account for daily work. Keep a separate administrator account for installing software.',
  'Only install software the Coordinator has approved.',
  'Check monthly that updates are installing and security software is active.'],
 ['Every computer is on a supported system with updates on.', 'Everyday accounts are not administrators.'],
 ['IRS Publication 4557', '16 CFR 314.4(c)']))

G.append(('wifi-router', 'Secure your router and guest Wi-Fi',
 'Change default passwords on your router and other network devices, keep their software current, and keep visitors on a separate network.',
 'Routers, printers and copiers ship with default passwords that are published online. A guest on your main Wi-Fi is on the same network as your client files.',
 ['Sign in to your router\'s admin page or app and change the default administrator password to a long, unique one stored in your password manager.',
  'Use WPA2 or WPA3 security with a strong Wi-Fi password. Turn off WPS and remote administration unless you need them.',
  'Turn on automatic firmware updates, or check for updates every few months.',
  'Create a guest network for visitors and personal devices, separate from the network your work computers use.',
  'Change default passwords on printers, copiers, scanners and network storage, and update their firmware.',
  'Do this at every location where firm equipment connects, including home offices.'],
 ['No network device uses its default password.', 'Visitors use a guest network.'],
 ['IRS Publication 4557']))

G.append(('efin-monitoring', 'Watch your EFIN during filing season',
 'Check each week during filing season how many returns have been filed under your EFIN, so you spot misuse early.',
 'Criminals who steal a preparer\'s credentials file fake returns under the firm\'s EFIN. The IRS recommends checking the count of returns filed with your EFIN regularly during filing season.',
 ['Sign in to IRS e-Services and open your e-File application to see your EFIN status and the number of returns filed.',
  'Set a weekly reminder from January through the October extension deadline.',
  'Compare the IRS count with the number your software shows you transmitted.',
  'If the IRS count is higher than yours, contact the IRS e-Help Desk right away and tell your Coordinator.',
  'Keep your e-File application current when staff, addresses or principals change.'],
 ['A weekly check is on the calendar for filing season.', 'Checks are noted (date and counts).'],
 ['IRS Publication 4557', 'IRS Publication 3112']))

G.append(('tabletop', 'Walk through your breach checklist',
 'Spend an hour once a year talking through a realistic incident using your plan, and fix what you find.',
 'The first hours of an incident are stressful. A practice run shows whether your contact list, steps and responsibilities actually work. The FTC Safeguards Rule requires a written incident response plan.',
 ['Gather the Coordinator, the backup and anyone with a role in the plan. Allow about an hour.',
  'Pick a scenario: a stolen laptop, a staff email account taken over, ransomware, or the IRS telling you fraudulent returns were filed under your EFIN.',
  'Walk through the incident response steps in your plan in order. Who notices? Who is called? What gets shut off? Who contacts the IRS Stakeholder Liaison, your insurer and affected clients?',
  'Check contact numbers in Attachment C are current.',
  'Note who must notify the FTC: an event involving unencrypted information of 500 or more consumers must be reported within 30 days of discovery. State notice rules also apply.',
  'Write down the date, who attended and what you\'ll change, and update the plan.'],
 ['A walkthrough in the past 12 months is recorded.', 'Fixes from it are made or scheduled.'],
 ['16 CFR 314.4(h)', '16 CFR 314.4(j)', 'IRS Publication 4557']))

G.append(('access-offboarding', 'Individual logins, access reviews and offboarding',
 'Give each person their own login with only the access they need, review access yearly, and remove it the day someone leaves.',
 'Shared logins make it impossible to tell who did what, and former staff with working passwords are a common source of breaches. The FTC Safeguards Rule requires limiting access to customer information to authorized users who need it.',
 ['Create a separate login for each person in every system, and stop using shared accounts.',
  'Give each person only the access their job needs.',
  'Once a year, list who can access each system and remove anyone who shouldn\'t.',
  'When someone leaves, on their last day: disable their logins, remove them from the password manager and shared vaults, change any shared passwords, collect devices and keys, and update your IRS e-File application if they were listed.',
  'Keep a short offboarding checklist and note the date each step was done.'],
 ['Everyone has their own login.', 'An access review in the past year is recorded.', 'Offboarding is done the same day.'],
 ['16 CFR 314.4(c)(1)', 'IRS Publication 4557']))

G.append(('ai-tools', 'Use AI tools without exposing client data',
 'Decide which AI tools may be used for client work, keep client information out of personal or free accounts, and write the rule down.',
 'Free and personal AI accounts may keep what you type and use it to train their models. Entering client tax information may also be a disclosure under IRC §7216. Business AI services can offer contract terms that protect your data.',
 ['List the AI tools anyone at the firm uses, including features built into other software.',
  'For each one, check whether it is a business account and whether its terms say your data isn\'t used for training and is protected.',
  'Approve the tools that meet those terms and add them to your vendor list. Treat them like any other provider.',
  'Write the rule: no client information in any AI tool that isn\'t approved, and no SSNs or full account numbers in any AI tool.',
  'Check with your adviser whether your use needs client consent under §7216.',
  'Train staff on the rule and review the list yearly.'],
 ['The approved AI tool list is written down.', 'Staff have been told the rule.'],
 ['IRC §7216', '16 CFR 314.4(f)']))

assert len(G) == 15 and len(set(g[0] for g in G)) == 15

def guide_page(fname, title, body, desc):
    doc = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{_h.escape(title)} | PlainWarden</title><meta name="description" content="{_h.escape(desc)}"><link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600;700;800&amp;display=swap">
<style>
body{{margin:0;background:#F5F6F3;color:#15212C;font-family:'Public Sans',system-ui,-apple-system,'Segoe UI',sans-serif;font-size:17px;line-height:1.65}}
a{{color:#1D5C47}} header{{background:#fff;border-bottom:1px solid #D5DAD6;padding:18px 16px}}
.wrap{{max-width:760px;margin:0 auto}} .brand{{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:#15212C;font-weight:800;font-size:21px}}
main{{padding:40px 16px 64px}} h1{{font-size:32px;line-height:1.2;margin:0 0 8px}} h2{{font-size:19px;margin:28px 0 6px}}
.lead{{font-size:19px;color:#2c3a46;margin:0 0 20px}} .muted{{color:#4A5865;font-size:15px}} li{{margin:6px 0}}
.box{{background:#fff;border:1px solid #D5DAD6;border-radius:6px;padding:6px 20px;margin:16px 0}} .done{{background:#EAF2EE;border-color:#1D5C47}}
.crumb{{font-size:15px;margin:0 0 12px}} .refs{{font-size:15px;color:#4A5865}}
footer{{border-top:1px solid #D5DAD6;padding:24px 16px;font-size:14px;color:#4A5865}} footer a{{margin-right:16px;display:inline-block;overflow-wrap:anywhere}}
</style></head><body>
<header><div class="wrap"><a class="brand" href="../index.html"><svg width="24" height="28" viewBox="0 0 28 32" aria-hidden="true"><path d="M14 1 L26 6 V15 C26 23 20.5 28.5 14 31 C7.5 28.5 2 23 2 15 V6 Z" fill="none" stroke="#1D5C47" stroke-width="2.4" stroke-linejoin="round"/><path d="M9 16 L12.5 19.5 L19.5 12" fill="none" stroke="#1D5C47" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>PlainWarden</a></div></header>
<main><div class="wrap">
{body}
<p class="muted">General guidance for small tax and accounting firms, last reviewed {GUIDES_REVIEWED}. It is not legal advice and does not certify compliance. Product menus change; check your provider's help pages for exact steps.</p>
</div></main>
<footer><div class="wrap"><a href="../index.html">Home</a><a href="index.html">Guides</a><a href="../terms.html">Terms</a><a href="../privacy.html">Privacy</a><a href="mailto:support@plainwarden.com">support@plainwarden.com</a></div></footer>
</body></html>'''
    open(OUT + '/guides/' + fname, 'w').write(doc)

for slug, title, summary, why, steps, done, refs in G:
    body = (f'<p class="crumb"><a href="index.html">How-to guides</a></p><h1>{_h.escape(title)}</h1><p class="lead">{_h.escape(summary)}</p>'
            f'<h2>Why it matters</h2><p>{_h.escape(why)}</p><h2>Steps</h2>{_ol(steps)}'
            f'<div class="box done"><h2 style="margin-top:12px">You\'re done when</h2>{_ul([_h.escape(d) for d in done])}</div>'
            f'<p class="refs"><b>References:</b> {_h.escape("; ".join(refs))}</p>')
    guide_page(slug + '.html', title, body, summary)

idx = ('<h1>How-to guides</h1><p class="lead">Short, practical steps for the safeguards small tax and accounting firms most often need to put in place.</p><div class="box"><ul>'
       + ''.join(f'<li><a href="{s}.html"><b>{_h.escape(t)}</b></a><br><span class="muted">{_h.escape(sm)}</span></li>' for s, t, sm, *_ in G) + '</ul></div>')
guide_page('index.html', 'How-to guides', idx, 'Practical security how-to guides for small tax and accounting firms.')
GUIDE_SLUGS = [g[0] for g in G]
