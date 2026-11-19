# Partner (affiliate and referral) program page. Executed by build_site.py after content.py (uses site_page, OUT).
# Applications go to a separate Tally form; approved partners get a ?ref=<code> link (see attribution.py).
PARTNER_FORM = 'https://tally.so/r/zEMAQa'
partners_body = (
  '<h1>PlainWarden partner program</h1>'
  '<p class="lead">Recommend PlainWarden to solo and small tax practices, and we pay you for every customer you send.</p>'
  '<p><a class="cta" href="' + PARTNER_FORM + '">Apply to be a partner</a></p>'
  '<h2>What we pay</h2>'
  '<div class="tw"><table><tr><th>When a customer you referred</th><th>You earn</th></tr>'
  '<tr><td>Buys the Plan ($89)</td><td>$30</td></tr>'
  '<tr><td>Buys Year One ($149 first year)</td><td>$50</td></tr>'
  '<tr><td>Renews Year One ($199 a year)</td><td>$20 each renewal</td></tr></table></div>'
  '<p class="muted">Commissions are paid monthly by ACH or PayPal once the 14-day refund window has passed. Refunded orders don\'t earn a commission. US partners provide a W-9.</p>'
  '<h2>How it works</h2><ol>'
  '<li>Apply with the short form. We reply within 2 business days.</li>'
  '<li>If approved, you sign a one-page partner agreement and get your personal link.</li>'
  '<li>Anyone who arrives through your link and buys within 60 days counts as your referral.</li>'
  '<li>Each month we email you what you earned and pay it.</li></ol>'
  '<h2>Who it suits</h2><ul>'
  '<li>IT and managed services providers who look after tax and accounting offices. The plan\'s action list is mostly IT work: MFA, backups, encryption, vendor reviews.</li>'
  '<li>Tax software consultants, trainers and continuing education providers.</li>'
  '<li>Bloggers, newsletter writers and creators who cover tax practice management.</li>'
  '<li>Bookkeepers, accountants and practice coaches with small-firm clients.</li></ul>'
  '<h2>Partner rules</h2><ul>'
  '<li>Say clearly that you earn a commission whenever you recommend PlainWarden.</li>'
  '<li>Describe PlainWarden accurately: it builds a written security plan from a firm\'s own answers. Don\'t say it makes a firm "compliant" or "certified", or that the IRS requires PlainWarden.</li>'
  '<li>No spam, no bidding on "PlainWarden" in search ads, and no coupon or deal sites.</li></ul>'
  '<p>Want to see what your referrals get? <a href="sample-plan.html">Look at a sample plan</a>.</p>'
  '<p><a class="cta" href="' + PARTNER_FORM + '">Apply to be a partner</a></p>'
  '<p class="muted">Questions: <a href="mailto:support@plainwarden.com">support@plainwarden.com</a>. The partner agreement governs if anything here differs from it.</p>'
)
_pcss = ('.cta{display:inline-block;background:#1D5C47;color:#fff!important;text-decoration:none;font-weight:700;padding:12px 20px;border-radius:6px;margin:6px 10px 6px 0}'
         'table{border-collapse:collapse;width:100%;font-size:16px;margin:8px 0;background:#fff}td,th{border:1px solid #D5DAD6;padding:8px 10px;text-align:left}th{background:#EAF2EE}.tw{overflow-x:auto}')
site_page('partners.html', 'Partner program', 'Earn $30 to $50 for each tax practice you refer to PlainWarden, plus $20 on every Year One renewal.', partners_body, _pcss)
# The shared template adds a guides disclaimer paragraph; it doesn't belong on this page.
_pp = OUT + '/partners.html'
_ps = open(_pp).read()
_ps = re.sub(r'<p class="muted">General guidance for small tax and accounting firms.*?</p>\n', '', _ps, count=1, flags=re.S)
open(_pp, 'w').write(_ps)
