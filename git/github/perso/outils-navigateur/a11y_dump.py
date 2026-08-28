"""Releve accessible de la page courante.

Un seul bout de JS, partage par les autres scripts : il liste les champs,
boutons et liens VISIBLES avec le libelle que lit reellement un lecteur
d'ecran (aria-label, label[for], label parent, aria-labelledby). C'est ce
libelle qu'on reutilise ensuite dans get_by_label / get_by_role, au lieu
de selecteurs CSS qui cassent des que la page est regeneree.
"""

DUMP_JS = r"""
() => {
  function labelFor(el) {
    if (el.getAttribute('aria-label')) return el.getAttribute('aria-label').trim();
    if (el.id) {
      const l = document.querySelector(`label[for="${el.id}"]`);
      if (l) return l.innerText.trim();
    }
    const pl = el.closest('label');
    if (pl) return pl.innerText.trim();
    const lb = el.getAttribute('aria-labelledby');
    if (lb) {
      const t = lb.split(' ').map(i => (document.getElementById(i) || {}).innerText || '').join(' ').trim();
      if (t) return t;
    }
    return '';
  }
  const visible = el => el.offsetParent !== null;

  const fields = [];
  document.querySelectorAll('input, textarea, select').forEach(el => {
    const type = el.getAttribute('type') || '';
    if (['hidden', 'submit', 'image'].includes(type)) return;
    if (!visible(el)) return;
    fields.push({
      tag: el.tagName.toLowerCase(),
      type,
      label: labelFor(el).slice(0, 60),
      placeholder: el.getAttribute('placeholder') || '',
      name: el.getAttribute('name') || '',
      id: el.id || '',
    });
  });

  const buttons = [];
  document.querySelectorAll('button, [role=button], a.btn').forEach(b => {
    const t = (b.innerText || b.getAttribute('aria-label') || '').trim();
    if (t && visible(b)) buttons.push(t.slice(0, 60));
  });

  const links = [];
  document.querySelectorAll('a[href]').forEach(a => {
    const t = (a.innerText || a.getAttribute('aria-label') || '').trim();
    if (t) links.push({ text: t.slice(0, 60), href: a.getAttribute('href') });
  });

  return { title: document.title, url: location.href, fields, buttons, links };
}
"""


def format_dump(d, max_links=60):
    """Rend le releve lisible en texte, pour ecriture dans un fichier."""
    out = [f"titre : {d['title']}", f"url   : {d['url']}", ""]
    out.append(f"CHAMPS ({len(d['fields'])}) :")
    for f in d["fields"]:
        out.append(
            f"  [{f['tag']}/{f['type']}] label={f['label']!r} "
            f"placeholder={f['placeholder']!r} name={f['name']!r} id={f['id']!r}"
        )
    out.append("")
    out.append(f"BOUTONS ({len(d['buttons'])}) :")
    out += [f"  {b!r}" for b in d["buttons"]]
    out.append("")
    out.append(f"LIENS ({len(d['links'])}, {max_links} premiers) :")
    out += [f"  {l['text']!r} -> {l['href']}" for l in d["links"][:max_links]]
    return "\n".join(out)
