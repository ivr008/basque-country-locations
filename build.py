#!/usr/bin/env python3
"""Generate index.html for 'Iconic Locations of the Basque Country'."""
import json, html
from urllib.parse import quote

META = json.load(open("meta.json"))

def ipath(slug):
    return META.get(slug, {}).get("path", "")

def credit(slug):
    m = META.get(slug, {})
    if not m:
        return ""
    page = "https://commons.wikimedia.org/wiki/" + quote(m.get("title", "").replace(" ", "_"))
    return (f'Photo: {html.escape(m.get("artist","Unknown"))} \u00b7 '
            f'<a href="{page}" target="_blank" rel="noopener">{html.escape(m.get("license","See source"))}</a>')

REGIONS = {
 "Bizkaia": "#c8102e",
 "Gipuzkoa": "#0b7a3b",
 "Araba": "#b06a00",
 "Navarre": "#6a2c8f",
 "Iparralde": "#1c6ea4",
}

LOCATIONS = [
 dict(slug="bilbao", name="Bilbao", alt="Bilbo", region="Bizkaia", tags=["City", "Culture"],
      desc="The largest city in the Basque Country and its cultural engine. Once a gritty industrial port, "
           "Bilbao reinvented itself as a capital of design and art, with a walkable Casco Viejo, a "
           "celebrated food scene and riverside promenades that draw you toward the Guggenheim."),
 dict(slug="guggenheim", name="Guggenheim Museum Bilbao", alt="Guggenheim Bilbao Museoa", region="Bizkaia", tags=["Art", "Architecture"],
      desc="Frank Gehry's titanium masterpiece, opened in 1997, turned a fading shipbuilding city into a "
           "global destination. Its shimmering, ship-like curves \u2014 guarded by Jeff Koons's giant "
           "\u201cPuppy\u201d \u2014 are the emblem of Bilbao's rebirth."),
 dict(slug="gaztelugatxe", name="San Juan de Gaztelugatxe", alt="Gaztelugatxe", region="Bizkaia", tags=["Natural Wonder", "Heritage"],
      desc="A stone hermitage perched on a tiny islet, reached by a winding stone bridge and 241 steps. "
           "Famous worldwide as \u201cDragonstone\u201d in Game of Thrones, it is the most dramatic spot on "
           "the Biscay coast."),
 dict(slug="mundaka", name="Mundaka", alt="Mundaka", region="Bizkaia", tags=["Coast", "Surf"],
      desc="A picture-postcard fishing village at the mouth of the Urdaibai estuary, home to one of Europe's "
           "most famous left-hand waves. Whitewashed houses and the little Santa Catalina chapel overlook "
           "the water."),
 dict(slug="guernica", name="Gernika", alt="Guernica", region="Bizkaia", tags=["History", "Heritage"],
      desc="The town immortalised by Picasso's Guernica after its bombing in 1937. Its Assembly House and "
           "the symbolic Tree of Gernika remain the beating heart of Basque self-government and identity."),
 dict(slug="vizcaya-bridge", name="Vizcaya Bridge", alt="Bizkaiko Zubia", region="Bizkaia", tags=["UNESCO", "Engineering"],
      desc="The world's oldest transporter bridge (1893) and a UNESCO World Heritage Site. It ferries cars "
           "and passengers across the Nervión estuary in a suspended gondola \u2014 a graceful feat of "
           "industrial-age engineering."),
 dict(slug="urdaibai", name="Urdaibai Biosphere Reserve", alt="Urdaibai", region="Bizkaia", tags=["Nature", "UNESCO"],
      desc="A UNESCO Biosphere Reserve where river, marsh and Atlantic coast meet. Its estuary and cliffs "
           "shelter rich birdlife and link the beaches, the villages of Mundaka and Bermeo, and the ancient "
           "cave of Santimamiñe."),
 dict(slug="san-sebastian", name="San Sebastián", alt="Donostia", region="Gipuzkoa", tags=["City", "Food"],
      desc="A belle-époque seaside jewel, famed for the perfect shell-shaped La Concha bay and one of the "
           "highest concentrations of Michelin stars on Earth. Elegant boulevards, pintxos bars and Mount "
           "Igueldo frame the view."),
 dict(slug="zumaia-flysch", name="Zumaia Flysch", alt="Zumaia", region="Gipuzkoa", tags=["Natural Wonder", "Geology"],
      desc="Layered rock formations that read like the pages of a giant book, recording 60 million years of "
           "Earth's history. The cliffs of Itzurun beach are a pilgrimage site for geologists and "
           "photographers alike."),
 dict(slug="hondarribia", name="Hondarribia", alt="Hondarribia", region="Gipuzkoa", tags=["Town", "Coast"],
      desc="A fortified border town opposite Hendaye, with a walled medieval centre, a castle that is now a "
           "parador, and a colourful fishermen's quarter right on the estuary."),
 dict(slug="onati", name="Oñati", alt="Oñate", region="Gipuzkoa", tags=["Heritage", "Town"],
      desc="Home to the oldest university in the Basque Country (1540). Its arcaded main square and "
           "Renaissance college make it one of the region's finest historic towns \u2014 and a gateway to "
           "the mountains of Arantzazu."),
 dict(slug="arantzazu", name="Sanctuary of Arantzazu", alt="Arantzazuko santutegia", region="Gipuzkoa", tags=["Heritage", "Art"],
      desc="A bold modern basilica set deep in the Aizkorri mountains, adorned with monumental sculptures by "
           "Jorge Oteiza and work by Eduardo Chillida. A spiritual and artistic landmark of the Basque "
           "cultural revival."),
 dict(slug="loyola", name="Sanctuary of Loyola", alt="Loiolako santutegia", region="Gipuzkoa", tags=["Heritage", "Spiritual"],
      desc="The birthplace of St. Ignatius of Loyola, founder of the Jesuits. The monumental baroque "
           "sanctuary, crowned by an immense gilded dome, is one of the grandest religious complexes in "
           "Spain."),
 dict(slug="vitoria-gasteiz", name="Vitoria-Gasteiz", alt="Gasteiz", region="Araba", tags=["City", "Green"],
      desc="The Basque Country's capital and a European pioneer of green urban living. Its medieval, "
           "almond-shaped old town and the Plaza de la Virgen Blanca sit beside a celebrated \u201cgreen "
           "ring\u201d of parks."),
 dict(slug="laguardia", name="Laguardia", alt="Guardia", region="Araba", tags=["Wine Country", "Heritage"],
      desc="A hilltop medieval town ringed by walls in the heart of the Rioja Alavesa wine country. Its "
           "bodegas, cobbled lanes and vineyard views make it the capital of Basque wine tourism."),
 dict(slug="anana", name="Salinas de Añana", alt="Añanako Gatz Harana", region="Araba", tags=["UNESCO", "Heritage"],
      desc="A rare inland salt valley with thousands of wooden evaporation terraces, worked since Roman "
           "times. This extraordinary, UNESCO-recognised landscape is one of the oldest salt-production "
           "sites in Europe."),
 dict(slug="pamplona", name="Pamplona", alt="Iruñea", region="Navarre", tags=["City", "Festival"],
      desc="Capital of Navarre and famous the world over for San Fermín, when runners sprint ahead of bulls "
           "through the streets. Its Gothic cathedral, star-shaped citadel and pintxos scene reward "
           "visitors all year round."),
 dict(slug="roncesvalles", name="Roncesvalles", alt="Orreaga", region="Navarre", tags=["Heritage", "Camino"],
      desc="A legendary pass on the Camino de Santiago, where Roland's epic battle was fought. Its Gothic "
           "collegiate church and monastery have welcomed weary pilgrims for a thousand years."),
 dict(slug="ujue", name="Ujué", alt="Uxue", region="Navarre", tags=["Village", "Heritage"],
      desc="A tiny hilltop village crowned by a fortified Romanesque church, offering sweeping views across "
           "Navarre. Its honey-coloured lanes feel frozen in the Middle Ages."),
 dict(slug="zugarramurdi", name="Zugarramurdi", alt="Zugarramurdi", region="Navarre", tags=["Legend", "Nature"],
      desc="A village of legend whose caves hosted the \u201cwitches of Zugarramurdi,\u201d tried by the "
           "Inquisition in 1610. The vast limestone cavern and its museum tell one of Europe's most famous "
           "witchcraft stories."),
 dict(slug="biarritz", name="Biarritz", alt="Miarritze", region="Iparralde", tags=["Coast", "City"],
      desc="The glamorous queen of the French Basque coast, once a favourite of Empress Eugénie and European "
           "royalty. Surf culture, a grand casino and the Rocher de la Vierge meet belle-époque elegance."),
 dict(slug="bayonne", name="Bayonne", alt="Baiona", region="Iparralde", tags=["City", "Food"],
      desc="A cultured river port known for its Gothic cathedral, half-timbered houses and \u2014 above all "
           "\u2014 its chocolate. Bayonne gave France its chocolate trade and remains a gourmet capital of "
           "the north."),
 dict(slug="saint-jean-de-luz", name="Saint-Jean-de-Luz", alt="Donibane Lohizune", region="Iparralde", tags=["Coast", "Town"],
      desc="A sheltered fishing port and royal wedding town, where Louis XIV married María Teresa in 1660. "
           "A crescent bay, colourful Basque houses and a lively old harbour make it irresistible."),
 dict(slug="la-rhune", name="La Rhune", alt="Larrun", region="Iparralde", tags=["Mountain", "Nature"],
      desc="The western Pyrenees' signature peak (905 m), climbed by a charming 1924 rack railway. "
           "Panoramic views sweep across the coast, the mountains and both sides of the French\u2013Spanish "
           "border."),
]

def card(l):
    p = ipath(l["slug"])
    tags = "".join(f'<span class="chip">{html.escape(t)}</span>' for t in l["tags"])
    return f"""
      <article class="loc" data-region="{html.escape(l['region'])}">
        <div class="loc-img">
          <img src="{html.escape(p)}" alt="{html.escape(l['name'])}" loading="lazy" />
          <span class="region-badge" style="--rc:{REGIONS[l['region']]}">{html.escape(l['region'])}</span>
        </div>
        <div class="loc-body">
          <h3>{html.escape(l['name'])}</h3>
          <div class="alt">{html.escape(l['alt'])}</div>
          <p>{html.escape(l['desc'])}</p>
          <div class="chips">{tags}</div>
          <div class="credit">{credit(l['slug'])}</div>
        </div>
      </article>"""

cards = "".join(card(l) for l in LOCATIONS)
filters = "".join(
    f'<button class="filter" data-f="{r}" style="--rc:{c}">{r}</button>'
    for r, c in REGIONS.items())

def credits_list():
    items = []
    for slug, m in META.items():
        page = "https://commons.wikimedia.org/wiki/" + quote(m.get("title", "").replace(" ", "_"))
        items.append(f'<li>{html.escape(m.get("artist","Unknown"))} \u2014 '
                     f'<a href="{page}" target="_blank" rel="noopener">{html.escape(m.get("license","See source"))}</a></li>')
    return "".join(items)

HERO = ipath("gaztelugatxe")
INTRO_IMG = ipath("zumaia-flysch")

LAUBURU = ('<svg class="lauburu" viewBox="0 0 100 100" aria-hidden="true">'
           + "".join(f'<path d="M50 50 C 46 30 54 14 78 10 C 64 26 60 38 50 50 Z" '
                     f'transform="rotate({a} 50 50)"/>' for a in (0, 90, 180, 270))
           + '</svg>')

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Iconic Locations of the Basque Country \u2014 Euskal Herria</title>
<meta name="description" content="A documented guide to the iconic locations of the Basque Country: cities, coast, mountains, art and heritage across Bizkaia, Gipuzkoa, Araba, Navarre and Iparralde." />
<meta property="og:title" content="Iconic Locations of the Basque Country" />
<meta property="og:description" content="Cities, coastlines, mountains and monuments of Euskal Herria." />
<meta property="og:type" content="website" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%97%BA%EF%B8%8F%3C/text%3E%3C/svg%3E" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet" />
<style>
  :root{{
    --cream:#f7f4ee; --paper:#ffffff; --ink:#20261f; --muted:#6b746a;
    --red:#c8102e; --green:#0b7a3b; --line:#e4ded2;
  }}
  *{{box-sizing:border-box}}
  html{{scroll-behavior:smooth; scroll-padding-top:74px}}
  body{{margin:0;background:var(--cream);color:var(--ink);
    font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
    line-height:1.65;-webkit-font-smoothing:antialiased}}
  img{{max-width:100%;display:block}}
  a{{color:inherit}}
  .wrap{{max-width:1200px;margin:0 auto;padding:0 clamp(1.1rem,4vw,2.5rem)}}
  h1,h2,h3{{font-family:"Playfair Display",Georgia,serif;margin:0}}

  nav.top{{position:sticky;top:0;z-index:50;background:rgba(247,244,238,.9);
    backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}}
  nav.top .inner{{max-width:1200px;margin:0 auto;padding:.7rem clamp(1.1rem,4vw,2.5rem);
    display:flex;align-items:center;justify-content:space-between;gap:1rem}}
  nav.top .logo{{display:flex;align-items:center;gap:.6rem;font-family:"Playfair Display",serif;
    font-weight:700;font-size:1.05rem;letter-spacing:.01em}}
  .lauburu{{width:22px;height:22px;fill:var(--red)}}
  nav.top a{{color:var(--muted);text-decoration:none;font-size:.82rem;font-weight:600;margin-left:1.1rem}}
  nav.top a:hover{{color:var(--ink)}}

  /* hero */
  .hero{{position:relative;min-height:80vh;display:flex;align-items:flex-end;overflow:hidden;
    background:#111}}
  .hero .bg{{position:absolute;inset:0;background-image:url('{html.escape(HERO)}');
    background-size:cover;background-position:center 40%}}
  .hero .shade{{position:absolute;inset:0;background:
    linear-gradient(180deg,rgba(15,20,15,.35),rgba(15,20,15,.72) 60%,rgba(15,20,15,.92))}}
  .hero .content{{position:relative;z-index:2;width:100%;padding:4rem 0 3rem;color:#fff}}
  .hero .eyebrow{{font-size:.76rem;font-weight:700;letter-spacing:.4em;text-transform:uppercase;
    color:#f4d58d;display:flex;align-items:center;gap:.6rem}}
  .hero .eyebrow .lauburu{{fill:#f4d58d;width:18px;height:18px}}
  .hero h1{{font-size:clamp(2.6rem,8vw,5.6rem);line-height:1.02;margin:.5rem 0 .3rem;font-weight:800}}
  .hero .sub{{font-family:"Playfair Display",serif;font-style:italic;font-size:clamp(1.2rem,3vw,1.9rem);
    color:#eadfce}}
  .hero .lead{{max-width:620px;color:#d9d5cc;margin:1rem 0 1.6rem}}
  .hero .cta{{display:flex;gap:.7rem;flex-wrap:wrap}}
  .btn{{display:inline-block;padding:.7rem 1.4rem;border-radius:999px;text-decoration:none;
    font-weight:700;font-size:.84rem;letter-spacing:.03em;background:#fff;color:var(--ink);transition:.2s}}
  .btn.alt{{background:var(--red);color:#fff}}
  .btn:hover{{transform:translateY(-2px)}}

  section{{padding:clamp(2.75rem,6vw,4.75rem) 0}}
  .sec-head{{margin-bottom:1.9rem;max-width:760px}}
  .sec-head .tag{{font-size:.74rem;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:var(--red)}}
  .sec-head h2{{font-size:clamp(2rem,5vw,3.2rem);margin:.2rem 0 .5rem;line-height:1.05}}
  .sec-head p{{color:var(--muted);margin:0}}

  /* intro */
  .intro{{display:grid;grid-template-columns:1.15fr .85fr;gap:2.5rem;align-items:center}}
  .intro p{{font-size:1.04rem;color:#3b423a;margin:0 0 1rem}}
  .intro figure{{margin:0;border-radius:1rem;overflow:hidden;border:1px solid var(--line);
    box-shadow:0 18px 40px rgba(30,30,20,.12)}}
  .intro figure img{{width:100%}}
  .intro figcaption{{font-size:.72rem;color:var(--muted);padding:.5rem .7rem;background:#fff}}

  /* facts */
  .facts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1rem}}
  .fact{{background:var(--paper);border:1px solid var(--line);border-radius:.9rem;padding:1.2rem 1.15rem}}
  .fact .k{{font-family:"Playfair Display",serif;font-size:1.5rem;font-weight:700;display:block}}
  .fact .l{{font-size:.8rem;color:var(--muted)}}
  .fact.r .k{{color:var(--red)}} .fact.g .k{{color:var(--green)}}

  /* filters */
  .filters{{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:1.6rem}}
  .filter{{border:1.5px solid var(--rc,#999);color:var(--rc,#333);background:transparent;
    border-radius:999px;padding:.45rem 1rem;font:inherit;font-size:.82rem;font-weight:700;cursor:pointer;
    transition:.18s}}
  .filter:hover{{background:color-mix(in srgb, var(--rc) 10%, transparent)}}
  .filter.active{{background:var(--rc,#333);color:#fff}}

  /* grid */
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:1.5rem}}
  .loc{{background:var(--paper);border:1px solid var(--line);border-radius:1rem;overflow:hidden;
    display:flex;flex-direction:column;box-shadow:0 10px 26px rgba(30,30,20,.06);transition:.25s}}
  .loc:hover{{transform:translateY(-5px);box-shadow:0 22px 46px rgba(30,30,20,.14)}}
  .loc.hide{{display:none}}
  .loc-img{{position:relative;aspect-ratio:16/10;overflow:hidden;background:#eee}}
  .loc-img img{{width:100%;height:100%;object-fit:cover;transition:transform .6s}}
  .loc:hover .loc-img img{{transform:scale(1.06)}}
  .region-badge{{position:absolute;top:.7rem;left:.7rem;background:var(--rc);color:#fff;
    font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
    padding:.28rem .6rem;border-radius:999px}}
  .loc-body{{padding:1.15rem 1.25rem 1.3rem;display:flex;flex-direction:column;flex:1}}
  .loc-body h3{{font-size:1.32rem;line-height:1.15}}
  .alt{{font-family:"Playfair Display",serif;font-style:italic;color:var(--red);font-size:.92rem;margin:.1rem 0 .6rem}}
  .loc-body p{{margin:0 0 1rem;color:#414840;font-size:.93rem}}
  .chips{{display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:.9rem}}
  .chip{{font-size:.68rem;font-weight:600;letter-spacing:.04em;text-transform:uppercase;
    color:var(--green);background:#e9f2ea;border-radius:999px;padding:.22rem .6rem}}
  .credit{{margin-top:auto;font-size:.66rem;color:#9a9f94}}
  .credit a{{color:#8a8f84;text-decoration:none;border-bottom:1px dotted #c9cec2}}

  .credits{{border-top:1px solid var(--line);margin-top:2rem;padding-top:1rem;color:var(--muted);font-size:.8rem}}
  .credits summary{{cursor:pointer;font-weight:600;color:var(--ink)}}
  .credits ul{{columns:2;column-gap:2rem;list-style:none;padding:0;margin:.6rem 0 0}}
  footer{{border-top:1px solid var(--line);padding:2rem 0;color:var(--muted);font-size:.8rem}}

  @media(max-width:820px){{
    .intro{{grid-template-columns:1fr}}
    .credits ul{{columns:1}}
    nav.top .links{{display:none}}
  }}
</style>
</head>
<body>

<nav class="top"><div class="inner">
  <div class="logo">{LAUBURU} Basque Country</div>
  <div class="links">
    <a href="#about">About</a><a href="#places">Locations</a><a href="#credits">Credits</a>
  </div>
</div></nav>

<header class="hero">
  <div class="bg"></div><div class="shade"></div>
  <div class="content wrap">
    <div class="eyebrow">{LAUBURU} Euskal Herria</div>
    <h1>The Basque Country</h1>
    <div class="sub">Iconic locations of a land between the mountains and the sea</div>
    <p class="lead">Twenty-four remarkable places across Bizkaia, Gipuzkoa, Araba, Navarre and Iparralde
      \u2014 from Frank Gehry's titanium museum and dragon-stone staircases to painted flysch cliffs,
      salt valleys and witch-caves.</p>
    <div class="cta">
      <a class="btn alt" href="#places">Explore the Locations</a>
      <a class="btn" href="#about">About the Region</a>
    </div>
  </div>
</header>

<!-- ABOUT -->
<section id="about"><div class="wrap">
  <div class="sec-head">
    <div class="tag">The Region</div>
    <h2>A country of seven provinces</h2>
  </div>
  <div class="intro">
    <div>
      <p>The Basque Country \u2014 <em>Euskal Herria</em>, \u201cthe land of the Basque speakers\u201d \u2014
      straddles the western Pyrenees where Spain meets France. It is home to the Basques, one of Europe's
      oldest peoples, with a language, <em>Euskara</em>, that is a mystery to linguists: a living isolate
      unrelated to any other tongue on Earth.</p>
      <p>Historically it counts seven provinces: <strong>Bizkaia</strong>, <strong>Gipuzkoa</strong>,
      <strong>Araba</strong> and <strong>Navarre</strong> in Spain, and <strong>Lapurdi</strong>,
      <strong>Zuberoa</strong> and <strong>Behe Nafarroa</strong> (together <em>Iparralde</em>) in France.
      The landscape runs from wild Atlantic surf beaches and fishing villages to green mountain valleys,
      vineyards and three of the country's great modern museums.</p>
      <p>Its people are fiercely proud of their identity \u2014 expressed in the red, green and white
      <em>Ikurriña</em> flag, the swirling <em>lauburu</em> symbol, the sport of <em>pelota</em>, and a
      culinary culture that has made San Sebastián one of the greatest places to eat on the planet.</p>
    </div>
    <figure>
      <img src="{html.escape(INTRO_IMG)}" alt="The flysch cliffs of Zumaia" />
      <figcaption>The flysch cliffs of Zumaia \u2014 60 million years of Earth history, on the Gipuzkoa coast.</figcaption>
    </figure>
  </div>
</div></section>

<!-- FACTS -->
<section style="padding-top:0"><div class="wrap">
  <div class="facts">
    <div class="fact r"><span class="k">7</span><span class="l">Traditional provinces</span></div>
    <div class="fact g"><span class="k">Euskara</span><span class="l">Europe's oldest language isolate</span></div>
    <div class="fact"><span class="k">3</span><span class="l">UNESCO listings featured here</span></div>
    <div class="fact g"><span class="k">1</span><span class="l">World-famous left-hand wave (Mundaka)</span></div>
    <div class="fact r"><span class="k">\u2248 3M</span><span class="l">Basque speakers &amp; residents</span></div>
    <div class="fact"><span class="k">Bay of Biscay</span><span class="l">Wild Atlantic coastline</span></div>
  </div>
</div></section>

<!-- LOCATIONS -->
<section id="places" style="padding-top:0"><div class="wrap">
  <div class="sec-head">
    <div class="tag">The Locations</div>
    <h2>Places worth crossing the world for</h2>
    <p>Filter by province or region. Colours match the badges on each place.</p>
  </div>
  <div class="filters">
    <button class="filter active" data-f="all" style="--rc:#20261f">All</button>
    {filters}
  </div>
  <div class="grid" id="grid">{cards}
  </div>
</div></section>

<div class="wrap" id="credits">
  <details class="credits">
    <summary>Image credits &amp; licences (\u00a9 their respective authors, via Wikimedia Commons)</summary>
    <ul>{credits_list()}</ul>
  </details>
  <footer>
    A fan-made, informational guide to the iconic locations of the Basque Country / Euskal Herria.
    Descriptions are provided in good faith; photographs are credited to their authors under their
    respective licences.
  </footer>
</div>

<script>
  const btns = document.querySelectorAll('.filter');
  const cards = document.querySelectorAll('.loc');
  btns.forEach(b => b.addEventListener('click', () => {{
    btns.forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    const f = b.dataset.f;
    cards.forEach(c => {{
      c.classList.toggle('hide', !(f === 'all' || c.dataset.region === f));
    }});
  }}));
</script>

</body>
</html>
"""
open("index.html", "w").write(HTML)
print("wrote index.html", len(HTML), "bytes,", len(LOCATIONS), "locations")
