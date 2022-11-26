from flask import jsonify
from flask import Flask,request
from serpapi import GoogleSearch
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)


params = {
  "engine": "google_scholar",
  "q": "biology",
  "api_key": "8d5e1e8fa8e972d18ea04c74af70775f48bf628bf2ee31df5d1f3c2d6d041059"
}
params1 = {
  "engine": "google_scholar_author",
  "author_id": "LSsXyncAAAAJ",
  "api_key": "8d5e1e8fa8e972d18ea04c74af70775f48bf628bf2ee31df5d1f3c2d6d041059"
}

searchResult = {
    "organic_results": [
    {
      "position": 0,
      "title": "Population biology of plants.",
      "result_id": "JC4Acibs_4kJ",
      "link": "https://www.cabdirect.org/cabdirect/abstract/19782321379",
      "snippet": "The first chapter is concerned with experiments, analogies and models. There are sections on dispersal, dormancy and recruitment of seedling populations, effects of neighbours, effects of predators and natural dynamics of plant populations, and plants, vegetation and evolution. There …",
      "publication_info": {
        "summary": "JL Harper - Population biology of plants., 1977 - cabdirect.org"
      },
      "inline_links": {
        "serpapi_cite_link": "https://serpapi.com/search.json?engine=google_scholar_cite&q=JC4Acibs_4kJ&token=a57f24e24842c7de",
        "cited_by": {
          "total": 14003,
          "link": "https://scholar.google.com/scholar?cites=9943926152122871332&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "9943926152122871332",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=9943926152122871332&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:JC4Acibs_4kJ:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3AJC4Acibs_4kJ%3Ascholar.google.com%2F",
        "versions": {
          "total": 6,
          "link": "https://scholar.google.com/scholar?cluster=9943926152122871332&hl=en&as_sdt=0,38",
          "cluster_id": "9943926152122871332",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cluster=9943926152122871332&engine=google_scholar&hl=en"
        },
        "cached_page_link": "https://scholar.google.comhttps://scholar.googleusercontent.com/scholar?q=cache:JC4Acibs_4kJ:scholar.google.com/+biology&hl=en&as_sdt=0,38"
      }
    },
    {
      "position": 1,
      "title": "Molecular cell biology",
      "result_id": "5BUDsdJ6ho0J",
      "link": "https://books.google.com/books?hl=en&lr=&id=K3JbjG1JiUMC&oi=fnd&pg=PA1&dq=biology&ots=arHdVTEq5F&sig=XpJrdZciq9Vy8ss_K4kJe7AnKk4",
      "snippet": "With its acclaimed author team, cutting-edge content, emphasis on medical relevance, and coverage based on landmark experiments, Molecular Cell Biology has justly earned an impeccable reputation as an authoritative and exciting text. The new Sixth Edition features …",
      "publication_info": {
        "summary": "H Lodish, A Berk, CA Kaiser, M Krieger, MP Scott… - 2008 - books.google.com"
      },
      "resources": [
        {
          "title": "nsysu.edu.tw",
          "file_format": "PDF",
          "link": "http://www2.nsysu.edu.tw/wzhlab/ch6.pdf"
        }
      ],
      "inline_links": {
        "serpapi_cite_link": "https://serpapi.com/search.json?engine=google_scholar_cite&q=5BUDsdJ6ho0J&token=5c469afb4977cc88",
        "cited_by": {
          "total": 9196,
          "link": "https://scholar.google.com/scholar?cites=10197973451558557156&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "10197973451558557156",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=10197973451558557156&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:5BUDsdJ6ho0J:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3A5BUDsdJ6ho0J%3Ascholar.google.com%2F",
        "versions": {
          "total": 18,
          "link": "https://scholar.google.com/scholar?cluster=10197973451558557156&hl=en&as_sdt=0,38",
          "cluster_id": "10197973451558557156",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cluster=10197973451558557156&engine=google_scholar&hl=en"
        }
      }
    },
    {
      "position": 2,
      "title": "Brock biology of microorganisms",
      "result_id": "aYK6cRyUoXoJ",
      "link": "https://www.researchgate.net/profile/Michael_Madigan/publication/48363170_Brock_Biology_of_Micro-Organisms/links/5573057208aeb6d8c017dcd8.pdf",
      "snippet": "Purple bacteria are anoxygenic phototrophs that grow phototrophically, obtaining carbon from CO2+ H2S (purple sulfur bacteria) or organic compounds (purple nonsulfur bacteria). Purple nonsulfur bacteria are physiologically diverse and most can grow as …",
      "publication_info": {
        "summary": "MT Madigan, JM Martinko, J Parker - 1997 - researchgate.net"
      },
      "resources": [
        {
          "title": "researchgate.net",
          "file_format": "PDF",
          "link": "https://www.researchgate.net/profile/Michael_Madigan/publication/48363170_Brock_Biology_of_Micro-Organisms/links/5573057208aeb6d8c017dcd8.pdf"
        }
      ],
      "inline_links": {
        "serpapi_cite_link": "https://serpapi.com/search.json?engine=google_scholar_cite&q=aYK6cRyUoXoJ&token=cbecc0298d3a04ca",
        "cited_by": {
          "total": 9710,
          "link": "https://scholar.google.com/scholar?cites=8836506793765667433&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "8836506793765667433",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=8836506793765667433&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:aYK6cRyUoXoJ:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3AaYK6cRyUoXoJ%3Ascholar.google.com%2F",
        "versions": {
          "total": 19,
          "link": "https://scholar.google.com/scholar?cluster=8836506793765667433&hl=en&as_sdt=0,38",
          "cluster_id": "8836506793765667433",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cluster=8836506793765667433&engine=google_scholar&hl=en"
        },
        "cached_page_link": "https://scholar.google.comhttps://scholar.googleusercontent.com/scholar?q=cache:aYK6cRyUoXoJ:scholar.google.com/+biology&hl=en&as_sdt=0,38"
      }
    },
    {
      "position": 3,
      "title": "Circular statistics in biology.",
      "publication_info": {
        "summary": "E Batschelet - ACADEMIC PRESS, 111 FIFTH AVE., NEW YORK, NY …, 1981"
      },
      "inline_links": {
        "cited_by": {
          "total": 6022,
          "link": "https://scholar.google.com/scholar?cites=15768135063984745093&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "15768135063984745093",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=15768135063984745093&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:hSoxK0yr09oJ:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3AhSoxK0yr09oJ%3Ascholar.google.com%2F",
      }
    },
    {
      "position": 4,
      "title": "Biology of amphibians",
      "result_id": "Bei1I16dqdMJ",
      "link": "https://books.google.com/books?hl=en&lr=&id=CzxVvKmrtIgC&oi=fnd&pg=PR9&dq=biology&ots=AZMakcrxfY&sig=_SM_ISg_pBl3qXSqEwMVxorAOSY",
      "snippet": "This is the widely acclaimed, preeminent reference and text on all aspects of amphibian biology, including their life history, ecology, morphology, and evolution. Copiously illustrated with original drawings and photographs and meticulously referenced with more than 2,500 …",
      "publication_info": {
        "summary": "WE Duellman, L Trueb - 1994 - books.google.com"
      },
      "inline_links": {
        "serpapi_cite_link": "https://serpapi.com/search.json?engine=google_scholar_cite&q=Bei1I16dqdMJ&token=cbecc0298d3a04ca",
        "cited_by": {
          "total": 7150,
          "link": "https://scholar.google.com/scholar?cites=15251894640718505989&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "15251894640718505989",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=15251894640718505989&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:Bei1I16dqdMJ:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3ABei1I16dqdMJ%3Ascholar.google.com%2F",
        "versions": {
          "total": 4,
          "link": "https://scholar.google.com/scholar?cluster=15251894640718505989&hl=en&as_sdt=0,38",
          "cluster_id": "15251894640718505989",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cluster=15251894640718505989&engine=google_scholar&hl=en"
        }
      }
    },
    {
      "position": 5,
      "title": "Elements of physical biology",
      "result_id": "-kzCxIbMYs0J",
      "link": "https://www.jstor.org/stable/43430362",
      "snippet": "F torn Dr. Alfred J. Lotka Dear Sir,-The review of Elements of Physical Biology which appeared in a recent issue of Science Progress is base on a fundamental misunderstanding of the method and purpos of that work. As this misunderstanding is calculated to mislead the …",
      "publication_info": {
        "summary": "AJ Lotka - Science Progress in the Twentieth Century (1919-1933 …, 1926 - JSTOR"
      },
      "inline_links": {
        "serpapi_cite_link": "https://serpapi.com/search.json?engine=google_scholar_cite&q=-kzCxIbMYs0J&token=cbecc0298d3a04ca",
        "cited_by": {
          "total": 5796,
          "link": "https://scholar.google.com/scholar?cites=14799616204691623162&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "14799616204691623162",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=14799616204691623162&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:-kzCxIbMYs0J:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3A-kzCxIbMYs0J%3Ascholar.google.com%2F",
        "versions": {
          "total": 2,
          "link": "https://scholar.google.com/scholar?cluster=14799616204691623162&hl=en&as_sdt=0,38",
          "cluster_id": "14799616204691623162",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cluster=14799616204691623162&engine=google_scholar&hl=en"
        }
      }
    },
    {
      "position": 6,
      "title": "Electron transfers in chemistry and biology",
      "result_id": "h-UUmfo_QI0J",
      "link": "https://www.sciencedirect.com/science/article/pii/030441738590014X",
      "snippet": "Electron-transfer reactions between ions and molecules in solution have been the subject of considerable experimental study during the past three decades. Experimental results have also been obtained on related phenomena, such as reactions between ions or molecules …",
      "publication_info": {
        "summary": "RA Marcus, N Sutin - Biochimica et Biophysica Acta (BBA)-Reviews on …, 1985 - Elsevier"
      },
      "inline_links": {
        "serpapi_cite_link": "https://serpapi.com/search.json?engine=google_scholar_cite&q=h-UUmfo_QI0J&token=cbecc0298d3a04ca",
        "cited_by": {
          "total": 8929,
          "link": "https://scholar.google.com/scholar?cites=10178205503399978375&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "10178205503399978375",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=10178205503399978375&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:h-UUmfo_QI0J:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3Ah-UUmfo_QI0J%3Ascholar.google.com%2F",
        "versions": {
          "total": 6,
          "link": "https://scholar.google.com/scholar?cluster=10178205503399978375&hl=en&as_sdt=0,38",
          "cluster_id": "10178205503399978375",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cluster=10178205503399978375&engine=google_scholar&hl=en"
        }
      }
    },
    {
      "position": 7,
      "title": "The world's worst weeds: distribution and biology",
      "publication_info": {
        "summary": "LG Holm, DL Plucknett, JV Pancho… - 1977 - University press of Hawaii Honolulu"
      },
      "inline_links": {
        "cited_by": {
          "total": 2884,
          "link": "https://scholar.google.com/scholar?cites=13741962940703055577&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "13741962940703055577",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=13741962940703055577&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:2R4wjXxCtb4J:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3A2R4wjXxCtb4J%3Ascholar.google.com%2F",
        "versions": {
          "total": 8,
          "link": "https://scholar.google.com/scholar?cluster=13741962940703055577&hl=en&as_sdt=0,38",
          "cluster_id": "13741962940703055577",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cluster=13741962940703055577&engine=google_scholar&hl=en"
        }
      }
    },
    {
      "position": 8,
      "title": "Free radicals in biology and medicine",
      "result_id": "GPYLddTNXkEJ",
      "link": "https://books.google.com/books?hl=en&lr=&id=3DlKCgAAQBAJ&oi=fnd&pg=PP1&dq=biology&ots=bonJ8_BujY&sig=iMkduC7cJ3EUnVEwMyH1cpUO164",
      "snippet": "Free Radicals in Biology and Medicine has become a classic text in the field of free radical and antioxidant research. Now in its fifth edition, the book has been comprehensively rewritten and updated whilst maintaining the clarity of its predecessors. Two new chapters …",
      "publication_info": {
        "summary": "B Halliwell, JMC Gutteridge - 2015 - books.google.com"
      },
      "resources": [
        {
          "title": "vanlanguni.edu.vn",
          "file_format": "PDF",
          "link": "http://thuvienso.vanlanguni.edu.vn/bitstream/Vanlang_TV/9963/11/SA3635_Free%20Radicals%20in%20Biology%20and%20Medicine_Chapter%207.pdf"
        }
      ],
      "inline_links": {
        "serpapi_cite_link": "https://serpapi.com/search.json?engine=google_scholar_cite&q=GPYLddTNXkEJ&token=cbecc0298d3a04ca",
        "cited_by": {
          "total": 26946,
          "link": "https://scholar.google.com/scholar?cites=15962228459898641425&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "15962228459898641425",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=15962228459898641425&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:EZzjdzY6hd0J:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3AGPYLddTNXkEJ%3Ascholar.google.com%2F",
        "versions": {
          "total": 7,
          "link": "https://scholar.google.com/scholar?cluster=15962228459898641425&hl=en&as_sdt=0,38",
          "cluster_id": "15962228459898641425",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cluster=15962228459898641425&engine=google_scholar&hl=en"
        }
      }
    },
    {
      "position": 9,
      "title": "Biology of ticks",
      "result_id": "k1yvQEA5qfMJ",
      "link": "https://books.google.com/books?hl=en&lr=&id=gck4AAAAQBAJ&oi=fnd&pg=PP1&dq=biology&ots=TbnHcyhX4b&sig=4v1XxtsrA506MvhTbGJyIWgSmrU",
      "snippet": "Biology of Ticks is the most comprehensive work on tick biology and tick-borne diseases. This second edition is a multi-authored work, featuring the research and analyses of renowned experts across the globe. Spanning two volumes, the book examines the …",
      "publication_info": {
        "summary": "DE Sonenshine, RM Roe - 2013 - books.google.com"
      },
      "inline_links": {
        "serpapi_cite_link": "https://serpapi.com/search.json?engine=google_scholar_cite&q=k1yvQEA5qfMJ&token=cbecc0298d3a04ca",
        "cited_by": {
          "total": 2123,
          "link": "https://scholar.google.com/scholar?cites=17557627570406513811&as_sdt=5,38&sciodt=0,38&hl=en",
          "cites_id": "17557627570406513811",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cites=17557627570406513811&engine=google_scholar&hl=en"
        },
        "related_pages_link": "https://scholar.google.com/scholar?q=related:k1yvQEA5qfMJ:scholar.google.com/&scioq=biology&hl=en&as_sdt=0,38",
        "serpapi_related_pages_link": "https://serpapi.com/search.json?as_sdt=0%2C38&engine=google_scholar&hl=en&q=related%3Ak1yvQEA5qfMJ%3Ascholar.google.com%2F",
        "versions": {
          "total": 8,
          "link": "https://scholar.google.com/scholar?cluster=17557627570406513811&hl=en&as_sdt=0,38",
          "cluster_id": "17557627570406513811",
          "serpapi_scholar_link": "https://serpapi.com/search.json?cluster=17557627570406513811&engine=google_scholar&hl=en"
        }
      }
    }
  ]
}

searchauthor ={
    "author":{   
    "name": "Cliff Meyer",
    "affiliations": "Dana-Farber Cancer Institute and Harvard T.H. Chan School of Public Health",
    "email": "Adresse email validée de jimmy.harvard.edu",
    "interests": [
      {
        "title": "Computational Biology",
        "link": "https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:computational_biology",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Acomputational_biology"
      },
      {
        "title": "Epigenetics",
        "link": "https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:epigenetics",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Aepigenetics"
      },
      {
        "title": "Gene Regulation",
        "link": "https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:gene_regulation",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Agene_regulation"
      },
    ],
    "thumbnail": "https://scholar.google.com/citations/images/avatar_scholar_128.png"
}
}
coAuthors = {
  "co_authors": [
    {
      "name": "Cliff Meyer",
      "link": "https://scholar.google.com/citations?user=LSsXyncAAAAJ&hl=en",
      "serpapi_link": "https://serpapi.com/search.json?author_id=LSsXyncAAAAJ&engine=google_scholar_author&hl=en",
      "author_id": "LSsXyncAAAAJ",
      "affiliations": "Dana-Farber Cancer Institute and Harvard T.H. Chan School of Public Health",
      "email": "Verified email at jimmy.harvard.edu",
      "thumbnail": "https://scholar.google.com/citations/images/avatar_scholar_56.png"
    },
    {
      "name": "Jason Carroll",
      "link": "https://scholar.google.com/citations?user=RsLo9p4AAAAJ&hl=en",
      "serpapi_link": "https://serpapi.com/search.json?author_id=RsLo9p4AAAAJ&engine=google_scholar_author&hl=en",
      "author_id": "RsLo9p4AAAAJ",
      "affiliations": "Group Leader, Cancer Research UK, University of Cambridge",
      "email": "Verified email at cancer.org.uk",
      "thumbnail": "https://scholar.google.com/citations/images/avatar_scholar_56.png"
    },
    {
      "name": "Housheng Hansen He",
      "link": "https://scholar.google.com/citations?user=XQI8DIEAAAAJ&hl=en",
      "serpapi_link": "https://serpapi.com/search.json?author_id=XQI8DIEAAAAJ&engine=google_scholar_author&hl=en",
      "author_id": "XQI8DIEAAAAJ",
      "affiliations": "Princess Margaret Cancer Centre, University Health Network; Department of Medical Biophysics",
      "email": "Verified email at uhnresearch.ca",
      "thumbnail": "https://scholar.googleusercontent.com/citations?view_op=small_photo&user=XQI8DIEAAAAJ&citpid=4"
    },
  ]
}
@app.route('/')
def index():
    return "hello"

@app.route('/query', methods = ['GET'])
def searchQuery():
    # print(type(searchresult))
# search = GoogleSearch(params)
    # results = search.get_dict()
    # organic_results = results["organic_results"]
    return jsonify(searchResult)

@app.route('/author', methods = ['GET'])
def searchAuthor():
    data = request.args.get('keyword')
    print(data)
    params2 = {
  "engine": "google_scholar_profiles",
  "mauthors": data,
  "api_key": "8d5e1e8fa8e972d18ea04c74af70775f48bf628bf2ee31df5d1f3c2d6d041059"
}

    search = GoogleSearch(params2)
    results = search.get_dict()
    profiles = results["profiles"]
    return jsonify(profiles)

@app.route('/coAuthor', methods = ['GET'])
def searchcoAuthor():
  author_id = request.args.get('author_id')
  print(author_id)
  params = {
  "engine": "google_scholar_author",
  "author_id": author_id,
  "api_key": "8d5e1e8fa8e972d18ea04c74af70775f48bf628bf2ee31df5d1f3c2d6d041059"
}
  search = GoogleSearch(params)
  results = search.get_dict()
  if 'co_authors' in results:
    co_authors = results["co_authors"]
    return jsonify(co_authors)
  else: 
    return 'No co-authors'

if __name__ == "__main__":
    app.run(debug=True)
    