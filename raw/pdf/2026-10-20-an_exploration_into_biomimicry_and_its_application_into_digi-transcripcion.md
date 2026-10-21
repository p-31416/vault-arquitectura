---
tipo: transcripcion
fecha: 2026-10-20
fuente_binaria: activos/fuentes/an_exploration_into_biomimicry_and_its_application_into_digi/An Exploration into Biomimicry and its Application into Digital and Parametric Architecture Design .pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\An Exploration into Biomimicry and its Application into Digital and Parametric Architecture Design .pdf
titulo: An Exploration into Biomimicry and its Application into Digital and Parametric Architecture Design
autor: PANCHUK
idioma: en
paginas: 203
palabras: 45223
metodo_extraccion: ghostscript-txtwrite
aviso: "Texto con copyright - uso interno del estudio. Citar con atribucion; no redistribuir."
tags: [pdf, raw, transcripcion, gaudi, bibliografia-ai, fair-use]
---

# Transcripción — An Exploration into Biomimicry and its Application into Digital and Parametric Architecture Design

> Texto extraído para análisis interno del estudio. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\An Exploration into Biomimicry and its Application into Digital and Parametric Architecture Design .pdf`. Binario local: [activos/fuentes/an_exploration_into_biomimicry_and_its_application_into_digi/An Exploration into Biomimicry and its Application into Digital and Parametric Architecture Design .pdf].
> Extracción: ghostscript-txtwrite · 203 págs · 45223 palabras. Copyright del original: se cita con atribución, no se redistribuye.

## [p. 1]

An Exploration into 

                   Biomimicry and its 

                 Application in Digital & 

               Parametric [Architectural] 

                        Design

                         A thesis

                presented to the University of Waterloo

                      in fulfi llment of the 

                 thesis requirement for the degree of

                     Master of Architecture

                          in

                        Architecture

                  Waterloo, Ontario, Canada, 2006

                     © Neal Panchuk 2006

## [p. 2]

_(página sin capa de texto)_

## [p. 3]

_(página sin capa de texto)_

## [p. 4]

_(página sin capa de texto)_

## [p. 5]

_(página sin capa de texto)_

## [p. 6]

Acknowledgements

              I would like to express my gratitude to everyone who has been by my side throughout the devel-

              opment of this thesis as well as my architectural training up to this point.  To my family and friends 

              for their support, understanding and constant presence in my life.

              I am indebted to those on my advisory panel including Philip Beesley, Michael Elmitt, and supervi-

              sor,  Thomas Seebohm for their time and effort.  Their knowledge and sensitivity to the practice 

              of architecture have provided unique insights and a constant frame of reference with which to 

              create this work.  To my external reader, Mark Burry, for taking time out of his busy schedule to 

              lend his expertise and wealth of experience to my thesis defense. 

              My thanks go out to Robert Aish, Rob Woodbury, and all the members of the GenerativeCom-

              ponents design team and Smart Geometry group for allowing me to be involved in the ongoing 

              development of parametric design software as well as the knowledge gained in my time spent at 

              the workshop and conference in London and Cambridge, UK and the Subtle Technologies work-

              shop in Toronto.

                                     vi

## [p. 7]

For my father

                          vii

## [p. 8]

_(página sin capa de texto)_

## [p. 9]

Contents                                                                                      Page

                    Preface                                                                                         1

                    1.0 Introduction                                                                                3

                     

                    1.1      Introduction to Biomimetics                                                            5

                    1.2      Direct Approach to Biomimetic Investigation                                            6

                    1.3      Indirect Approach to Biomimetic Investigation                                          7

                    1.4      Biomimetic Solutions in Other Design Disciplines                                       9

                    2.0      Exploration of Biomimetic Design Principles                                           11

                    2.1 Self Assembly                                                                              12

                             2.1.1    DNA and Genetic Coding                                                       12

                             2.1.2    Self Assembly in Nature                                                      13

                             2.1.3 Molecular Self Assembly                                                         13

                             2.1.4 Structural Development                                                          13

                             2.1.5    Endoskeletons and Exoskeletons                                               15

                    2.2      The Power of Shape                                                                    16

                             2.2.1    Fundamentals of Natural Form                                                 16

                             2.2.2    Forms that Organisms in Nature are Composed Of                               18

                             2.2.3    Forms of Structures that Organisms Build                                     19

                             2.2.4 Flatness                                                                        20

                             2.2.5 Surfaces                                                                        23

                             2.2.6 Angles and Corners                                                              23

                             2.2.7 Stiffness and Flexibility                                                       25

                             2.2.8 Increases in Scale                                                              25

                    2.3 Resilience and Healing                                                                     26

                    2.4 Materials as Systems                                                                       26

                    2.5      Sensing and Responding                                                                26

                             2.5.1    Static and Dynamic Structures                                                26

                             2.5.2    Natural Development of Form                                                  27

                                                                      ix

## [p. 10]

3.0      Biomimetic Principles of Form in Architecture                                              29

                               3.1 Built Examples                                                                                  30

                               3.2 Unbuilt Examples                                                                                33

                               3.3      Use of Structural Form in Architecture                                                     35

                               4.0      Investigation Into Surfaces and Manufacturing                                              39

                               4.1      Curved Surfaces – Defi nition, Generation and Analysis                                     40

                                        4.1.1 Surface Curvature                                                                    40

                                        4.1.2    Gaussian and Mean Curvature                                                       40

                                        4.1.3    Curvature Investigation and Representation                                        41

                                        4.1.4    Conical Sections and Surfaces Derived from Them                                   41

                                        4.1.5    Ruled and Developable Surfaces                                                    42

                                        4.1.6 Complex Surfaces                                                                     43

                               4.2      Primary Structural and Construction Specifi c Considerations                               44

                                        4.2.1 Construction Considerations                                                          44

                                        4.2.2 Structural Considerations                                                            44

                               4.3      Defi ning Surface Shapes                                                                   45

                                        4.3.1    Digital Form Generation Techniques and Shape Generation                           45

                                        4.3.2    Physical Model to Digital Model                                                   46

                                        4.3.3    Form Finding Through Structural Viability                                         47

                                        4.3.4    Structure and Enclosure                                                           47

                                        4.3.5    Approaches to Building a Large Compound Curved Surface                            48

                               4.4      Structural Surfaces – Translation from Digital Design to Physical Fabrication              48

                                        4.4.1    Large Continuous Surfaces                                                         49

                                        4.4.2 Small Continuous Surfaces                                                            50

                                        4.4.3 Surface Enclosure                                                                    51

                                        4.4.4    Thin Sheet Surfaces                                                               49

                                        4.4.5 Bendable Strips                                                                      51

                                                                                   x

## [p. 11]

4.4.6 Aggregated Faceted Panels                                                            53

                               4.4.7    Shaped Primary Structural Elements                                                54

                     5.0 Design Proposal                                                                                  57

                     5.1 Design Approach                                                                                  58

                     5.2 Design Objectives                                                                                59

                     5.3 Design Requirements                                                                              60

                     5.4 Design Methodology                                                                               60

                     5.5 Design Drivers                                                                                   61

                     6.0 Thesis Resolution                                                                                63

                     6.1       Design Concept #1 - Design Methodology                                                     64

                               6.1.1    A Natural Order                                                                   65

                               6.1.2    The Relevance of Parametric Design                                                67

                               6.1.3 Parametric Correlation                                                               68

                               6.1.4 GenerativeComponents                                                                 68

                                6.1.4.1 An Outline                                                                        68

                                6.1.4.2 Programmatic Description                                                          69

                                6.1.4.3 Terms                                                                             70

                                        6.1.4.4  An Illustrative Example of the GenerativeComponents System               73

                               6.1.5    Parametric Modeling Based on the Biological Genome                                78

                               6.1.6    Parametric Design and BIM (Building Information Modeling)                         89

                               6.1.7    Additional Areas for Further Research                                             91

                                        6.1.7.1 Genetic Algorithms                                                        91

                                6.1.7.2 Rule Based Programming                                                            91

                                6.1.7.3 Nanotechnology                                                                    92

                     6.2       Design Concept #2 – Ruled Surface Structure                                                93

                               6.2.1 Inspiration                                                                          93

                               6.2.2 Design Outline                                                                       95

                               6.2.3 Design Product                                                                       97

                               6.2.4 Design Evaluation                                                                   104

                                                                         xi

## [p. 12]

6.3      Design Concept #3 - Folded Chevron Structure                                          108

                                      6.3.1 Inspiration                                                                     108

                                      6.3.2 Design Outline                                                                  109

                                      6.3.3 Design Product                                                                  111

                                      6.3.4 Design Evaluation                                                               121

                              

                             7.0      Discussion and Conclusion                                                             125

                                  7.1  Discussion                                                                           126

                                  7.2  Conclusion                                                                           128

                                  

                             Appendix

                              A1. Design Concept #1 - GenerativeComponents Script File for 6.1.4.4                          133

                                       Illustrative Example 

                              A2. Design Concept #2 - GenerativeComponents Script File for Ruled                            137

                               Surface Structure

                              A3. Design Concept #3A - GenerativeComponents Script File for Static                          152

                                               Deployment of chevron_feature01

                              A4. Design Concept #3A - GenerativeComponents Script File for                                 159

                                               Static Deployment - Application of chevron_feature01 to Variable   

                                       BsplineSurface

                              A5. Design Concept #3B - GenerativeComponents Script File for                                 163

                                               Application of Dynamic Deployment

                             Glossary                                                                                       173

                             References                                                                                     175

                                                                              xii

## [p. 13]

Illustrations

                      Chapter 1

                      1.       Map of Biomimetic Processes.  Reproduced from Vincent, 2002, Chapter 3, p4.

                      2.       Rounded pleats of automobile air fi lter inspired from a dolphin’s nose.

                        (http://www.afefi lters.com/technology.htm)

                      3.       Pultrusion machine for carbon fi ber.

                        (http://www.bedfordplastics.com/images/pultrusion-machine.jpg)

                      4.       High magnifi cation of velcro hooks.

                        (http://www.seeingscience.cclrc.ac.uk/Activities/SeeingScience/Light/media.les 

                        son1.  Velcro%20hooks.jpg)

                      Chapter 2

                      5.       Self assembly of inorganic nanoclusters.  

                        (http://www.darkwing.uoregon.edu/~chem/dwjohnson.html)

                      6.       Process illustrating the evolution from path to surface, and pattern to structure.  From  

                        Bell and Vrana, Digital Tectonics:  Structural Patterning of Surface.

                       

                      7.       Structural analysis of shell comprised of radial and random patterns.  From Bell and  

                        Vrana,  Digital Tectonics:  Structural Patterning of Surface.

                      8.       Human Endoskeleton. (http://users.tinyworld.co.uk)

                      9.       Crab Exoskeletion. (http://www.odu.edu)

                      10.      Surface Area and Volume Correlation for Sphere and Cube.  Author.

                      11.      Cross-section of Bird Bone. 

                        (http://uk.dk.com/static/cs/uk/11/clipart/sci_animal/image_sci_animal029.html)

                      12.      Effects of Wind and Live Load on Structure.  Reproduced from Tsui, 1999.

                      13.      Effects of Live Load on Structure.  Reproduced from Tsui, 1999.

                      14.      Human Skull.  (http://images.google.ca/images)

                                                                           xiii

## [p. 14]

15.       Human Femur.  (http://biomech.me.unr.edu/hip.htm)

                               16.       Scallop Shell.  (www.bmyersphoto.com/BWXRAY/animals43.html)

                               17.       Snail Shell.  (http://images.google.ca/images)

                               18.       Tardigrade.  (http://images.google.ca/images)

                               19.       Sunfl ower.  (http://images.google.ca/images)

                               20.       Shell.  (http://images.google.ca/images)

                               21.       Spittlebug cocoon.  (http://images.google.ca/images)

                               22.       Ant nest.  (http://images.google.ca/images)

                               23.       Weaverbird Nest.  (http://images.google.ca/images)

                               24.       Spiderweb.  (http://images.google.ca/images)

                               25.       Termite tower.  (http://images.google.ca/images)

                               26.       Plant leaf.  (http://images.google.ca/images)

                               27.       Dragonfl y wing.  (http://images.google.ca/images)

                               28.       Cactus.  (http://images.google.ca/images)

                               29.       Surface Tension in Cylindrical and Spherical Vessels.  

                                 (http://hyperphysics.phy-astr.gsu.edu/hbase/ptens.html#lap)

                               30.       Relationship between radius and tension.  

                                 (http://hyperphysics.phy-astr.gsu.edu/hbase/ptens.html#lap)

                               31.       Human pelvis.  (http://biology.clc.uc.edu/Bone_Features.html)

                                                                                     xiv

## [p. 15]

32.      Rounded corners in tree branches. 

                        (www.photo.net/photo/pcd1628/point-lobos-tree-25)

                      33.      Stress localization and corner cracking.  (http://images.google.ca/images)

                      34.      World Trade Towers.  (http://images.google.ca/images)

                      35.      Tree in hurricane conditions.  (http://images.google.ca/images)

                      36.      Cross-section of Douglas Fir Cells.  

                        (www.mmat.ubc.ca/units/mmat/emlab/customers.asp)

                      37.      Cross section of vascular bundle in wood (xylem cells visible).   

                        (http://www.nexusresearchgroup.com/fun_science/emscope.htm)

                      38.      Cross-section of shell matrix.  (http://www.ucmp.berkeley.edu/esem/shell.gif)

                      39.      Detail of shell mollusk microstructure.  (http://www.ucmp.berkeley.edu/esem/shelstr.gif)

                      Chapter 3

                      40.      Sagrada Familia.  

                        (http://www.houstonarchitecture.info/haif/lofi version/index.php/t280.html)

                      41.      Palazzetto dello Sport.  

                        (http://www.promolegno.com/convegno/archivio/Venezia-Mestre/)

                      42.      Tsui’s Ecological House of the Future.  

                        (http://www.tdrinc.com/images/photos/large/ecol_E092.jpg)

                      43.      Yeang’s bioclimatic skyscraper.  

                        (www.srmassociates.com/Green.htm)

                      44.      Testa’s carbon tower.  (http://www.pubs.asce.org/ceonline/ceonline03/0403ce.html)

                      45.      EMERGENT Architecture’s radiant hydronic house.  

                        (http://www.emergentarchitecture.com/projects.php?id=6)

                                                                           xv

## [p. 16]

46.       EMERGENT Architecture’s lattice house.  

                                 (http://www.emergentarchitecture.com/projects.php?id=8)

                               47.       NOX:  A-life, an earlier version of Son-O-house.  From Spuybroek, L.  Nox. D-tower. 161.

                               48.       NOX:  Structural ribs defi ning a doubly-curved surface are clad in narrow woods strips  

                                                   the follow the curvature much like in shipbuilding.  From Spuybroek, L.  Nox.   

                                 Soft Offi ce. 233.

                               49.       NOX:  Design for the European Central Bank based on Radiolaria morphology.  From  

                                 Spuybroek, L.  Nox.  ECB. 291.

                               50.       Ernst Haeckel’s drawing of Radiolaria from the Family Spongurida.  

                                 (http://www.biologie.uni-hamburg.de/b-online/radio/Tafel_26.jpg)

                               Chapter 4

                               51.       Curvature of surfaces:  normal curvature and related principal values of a synclastic sur 

                                                   face (Reproduced from Schodek et. al, Digital Design and Manufacturing). 196.

                               52.       Curvature analysis diagram.  (http://images.google.ca/images)

                               53.       Ruled surfaces.  

                               54.       Roof of Nervi’s Palazzetto dello Sport which exhibits membrane action.  

                                 (http://images.google.ca/images)

                               55.       Strategies to support complexly shaped surfaces (Reproduced from Schodek et. al,   

                                 Digital Design and Manufacturing). 54.

                               56.       Directional layers of fi berglass laminated to a formed balsa core.  

                                 (www.northernatlanticdive.com)

                               57.       Relationships between skin and structure for complex surfaces.  (Reproduced from  

                                 Schodek et. al, Digital Design and Manufacturing). 56.

                               58.       Thermal Plate Forming.  Courtesy of Dies & Stamping News.  7/26/05.

                                                                                     xvi

## [p. 17]

59.       Fish Sculpture, Barcelona.  Photo by J. Scott Smith, courtesy of Frank O. Gehry & Associ-

                      ates.  2005.

                      60.       Swiss Re Headquarters, London.  Photo courtesy of Foster and Partners.  2005.  

                        (www.fosterandpartners.com)

                      61.       Surface subdivisions.  (Reproduced from Schodek et. al, Digital Design and 

                        Manufacturing).  200.

                      62.       Experience Music Project, Seattle.  Frank O. Gehry and Associates.  

                        (http://www.zverina.com/i/photography-seattle.htm)

                      Chapter 6

                      Note:  All diagrams in Chapter 6 by author except as noted.

                      63.       Tree diagram showing typical hierarchical relationship. for solid modeling operations.   

                        (www.cs.technion.ac.il/~irit/user_man.html)

                      64.       Tree diagram showing a composite hierarchical approach.

                      65. GC Symbolic View

                      66.       GC Line component and associated properties

                      67.       GC transactionFile view

                      68.       GC Graphical User Interface (GUI)

                      69.       GC Symbolic view and Model view

                      70.       Defi nition of Graph Variables.

                      71.       Defi nition of Point01.

                      72.       Point01 in the Symbolic, TransactionFile and Model views.

                                                                           xvii

## [p. 18]

73.       Defi nition and property expression for Line01.

                               74.       Graph Variable Building_Width changed.

                               75.       Symbolic view of component dependencies.

                               76.       Offset of Line03 from Line01.

                               77.       Symbolic view of model and dependencies for Line05.

                               78.       View of GC Script Editor and relevant programming code.

                               79.       Symbolic view of component dependencies.

                               80. TransactionFile view

                               81. GCScript Editor

                               82. Model View.

                               83.       Symbolic view of component dependencies.

                               84.       24-Color 3D FISH (Fluorescence in situ hybridization) Representation and Classifi    

                                         cation of Chromosomes in a Human G0 Fibroblast Nucleus.  

                                 (http://biology.plosjournals.org/archive/1545-7885/3/5/fi gure/10.1371_journal. 

                                 pbio.0030157.g001-L.jpg)

                               85.       Protein model showing varying levels of amino acid detail and information based on  

                                                   analytic requirements.  (http://ruppweb.dyndns.org/Xray/tutorial/pdb/helices.gif)

                               86.       Diagram of relationship between genotype and phenotype.  The genes (1-5) on the  

                                                   left govern the formation of a gene product (1 gene - 1 polypeptide).  A gene  

                                                   product can affect a number of features.  A phenotype may be the result of  

                                                   the combined effects of several gene products.  

                                 (www.biologie.uni-hamburg.de/b-online/e14/1.htm)

                                                                                    xviii

## [p. 19]

87.      GenerativeComponents Point component and the subset of update methods by which  

                                         the Point is recalculated.

                      88.      Primary protein structure.  The amino acid chain is a long sequence of amino acids.   

                        (http://cwx.prenhall.com/horton/medialib/media_portfolio/text_images/FG04_ 

                        01.JPG)

                      89.      Universal Genetic Code specifying relationship between the nucleotide bases and the  

                                         amino acids derived from them.  The information contained in the nucleotide  

                                         sequence of the mRNA is read as three letter words (triplets), called codons.   

                        (http://gslc.genetics.utah.edu/units/basics/transcribe/)

                      90.      GenerativeComponents transaction fi le.

                      91.      Secondary structure of protein molecule.  

                        (http://cwx.prenhall.com/horton/medialib/media_portfolio/text_images/FG04_ 

                        01.JPG)

                      92.      G-Code for milling machine operation.  The coding specifi es a number of different 

                                         operations or requirements that the machine is required to perform.  

                        (http://www.afog.com/images/gcode.jpg)

                      93.      Tertiary structure of protein molecule.  

                        (http://cwx.prenhall.com/horton/medialib/media_portfolio/text_images/FG04_ 

                        01.JPG)

                      94.      Quaternary structure of protein molecule.  

                        (http://cwx.prenhall.com/horton/medialib/media_portfolio/text_images/FG04_ 

                        01.JPG)

                      95. Structural elements.

                      96.      Adaptive panel cladding system

                      97.      Head of the human femur in section.  From Thompson, D.  On Growth and Form.  977.

                      98.      Crane-head and femur.  From Thompson, D.  On Growth and Form.  978.

                                                                           xix

## [p. 20]

99.       Diagram of stress-lines in the human foot.  From Thompson, D.  On Growth and Form.   

                                 980.

                               100.      Dragonfl y wing.  (http://images.google.ca/images/dragonfl y)

                               101.      Primary and secondary veins of dragonfl y.

                               102. Graph Variables

                               103.      Layout parameters and defi ning curves.

                               104.      YZ Planes and the resulting BsplineSurface and primary structural member layout lines.

                               105.      XZ Planes and the resulting secondary/tertiary layout lines derived from the 

                                 BsplineSurface.

                               106.      Extrusion of the primary and secondary/tertiary members in the Y direction.

                               107.      Direction of translation and associated decrease in wall thickness.

                               108.      UV Points on BsplineSurface

                               109.      Surface panels on BsplineSurface

                               110.      Point grid created based on location of the primary elements

                               111.      Surface panels created from projection of point grid onto the BsplineSurface

                               112.      ConstructionDisplay is added with text for location of the panels on the facade.

                               113.      Detail of ConstructionDisplay and text style applied to the panels for export to 

                                 FabricationPlanning.

                               114.      Flattened panels ready for laser cutting in the FabricationPlanning fi le.

                               115.      Detail of text style applied to panels for ease of identifi cation and optional scribing 

                                 by laser. 

                                                                                     xx

## [p. 21]

116.     Instantaneous translation of building confi guration

                    117.     Instantaneous translation of building confi guration

                    118.     Rendering of potential building confi guration.

                    119.     Right hind wing of Priacma Serrata (bleach beetle) showing folding pattern and the 

                                      major veins (RA & MP).  From Haas, F.  Wing folding in insects: A natural, 

                                      deployable structure.  2.

                    120.     Digitized folding pattern of Cantharis Livida.  Haas, F.  Wing folding in insects: A natural,  

                      deployable structure. 4.

                    121.     Basic mechanism of four panels connected by four folding lines that intersect at one  

                                      point.  Most complex folding patterns consist of a combination of several basic  

                                      mechanisms.  Haas, F.  Wing folding in insects: A natural, deployable structure. 4.

                    122.     Miura-ori pattern & Hornbeam leaf blooming.  

                    123.     Folded sheet with Miura-ori pattern.  From Basily, B. B., and E. A.  A continuous folding 

                                      process for sheet materials. 1.

                    124.     Continuous sheet folding machine.  From Basily, B. B., and E. A.  A continuous folding 

                                      process for sheet materials. 11.

                    125.     Continuous sheet folding machine.  From Basily, B. B., and E. A.  A continuous folding 

                                      process for sheet materials. 13.

                    126. Graph Variables.

                    127. Initial BsplineSurface.

                    128.     UV Points on BsplineSurface.

                    129.     Offset points from UV points.

                    130.     Chevron facet development

                                                                     xxi

## [p. 22]

131.     Full chevron facet surface.

                             132.     Generate Feature Type Interface.

                             133.     Application of chevron component to Design Concept #2

                             134.     Sequence of renderings showing facade reconfi guration and instantaneous chevron 

                               component update.

                             135.     Sequence of renderings showing canopy reconfi guration and instantaneous 

                               chevron component update.

                             136. Graph Variables.

                             137.     One unit of chevron quintet with numeric variables.

                             138.     Progressive development of chevron facets.

                             139.     Chevron inputs for update method.

                             140.     Population of baseCS with chevron components.

                             141.     Dynamic movement of chevron units.

                             142.     Symbolic view of chevron component derivation and relationships.

                                                                              xxii

## [p. 23]

Preface

        Architecture through its very nature is heavily involved in the development and integration of 

        two key aspects of the built environment, those being form and function.  For centuries, the 

        dominant form of structure has been strongly infl uenced by the current technology available in 

        the construction and manufacturing industry.  With the proliferation of mass production and the 

        development of the assembly line it became possible to create a construction industry based 

        on discrete building assemblies and materials that serve to benefi t a faster and easier method of 

        raising structures.  This increase of speed and relative ease of design due to unitization and stan-

        dardization has come at the cost of maximal structural effi ciency, minimization of materials and 

        a relative compensatory need to artifi cially regulate the interior building environment.  Recent 

        advances in computer modeling and systems testing have allowed the architect to improve upon 

        all of these aforementioned building variables.  However, without a fi rst principles approach to 

        design that questions the validity of the structures and systems to which these new technologies 

        of design and testing are applied, the whole process becomes burdened with an ineffi ciency that 

        will always be inherent.  The simple reason of advancement in a particular fi eld is not an a priori 

        reason for believing that the direction that fi eld is going in will yield the most profound and boun-

        tiful results.

        Like languages, architecture is a discipline that will always comprise a number of variations that 

        are characteristic of the people, social and geographic climate that they serve.  While this may be 

        true, there is an underlying basis by which all of these variations may be linked together whether 

        through a biological necessity to communicate with each other, as with language, or a similar bio-

        logical desire for shelter.  It is important to note here that each variant has both benefi ts and 

        detractions as compared to its siblings.  With architecture a number of intellectual and design phi-

        losophies have developed through time with some that remain and others that fall out of favour.  

        For any object or idea to endure and in effect become timeless it must pass through a number 

        of fi lters that measure its clarity and depth.  If the characteristics derived are deemed valuable 

        then what remains is a base that can be built upon and ultimately give rise to progeny that, while 

        unique unto themselves, still retain the genetic makeup from which they stemmed.

        In nature this has been well documented through the works of pioneers in the fi eld of biology 

        and evolution.  Over many millennia the organisms that inhabit this planet have gone through 

        countless environmental fi lters that have shaped and continue to inform the shape of organisms 

        today.  From early iterations to today’s counterparts the wealth of biological diversity is staggering 

        and is testament to the earth’s testing ground.  As supremely motivated and inquisitive creatures, 

                           1

## [p. 24]

gained from our ancestors.  This intellectual base is constantly refi ned and rethought in an effort 

           to sift through what is deemed unnecessary and excess and arrive at a new level of understand-

           ing and ability.  Nature has provided this framework of constant improvement for us and it is this 

           feature that is the basis for this thesis.  The principle of biomimetics strives to learn how nature 

           has learned and to not necessarily imitate but distill from nature the qualities and characteristics 

           of natural form and systems that may be applicable to our interpretation of architecture.

           My interest in the correlation between architecture and biology fi rst developed during my time at 

           McMaster University where I completed a Bachelor of Science specializing in biology.  The knowl-

           edge gained in the area of genetics and biological form prompted an inquisition into the relevance 

           of nature’s method of design and construction with regard to human constructions.  

                              2

## [p. 25]

1.0    Introduction

                 BIO–MIMICRY   [From the Greek bios, life, and mimesis, 

                 imitation] (Benyus 1997)

                 The emulation or imitation of natural forms, structures and 

                 systems [in design and construction] that have proven to be 

                 optimized in terms of effi ciency as a means to an end.

                           3

## [p. 26]

A biomimetic approach to design, while emu-          amount of instructions, documentation and 

                             lating natural systems, derives its solutions        visualization necessary to produce architec-

                             through the utilization of a design process          tural works.  

                             that seeks to satisfy the core requisites of a 

                             design in a holistic manner.  This approach          The design portion of the thesis will concen-

                             avoids a sequential component design process         trate on creating three design concepts that 

                             and attempts to develop the design products          will be developed based on varying levels of 

                             in a concurrent manner whereby necessary             granularity with respect to the scope of biomi-

                             changes that occur in the development of a           metic design in architecture.  The purpose of 

                             particular design component will be propa-           this investigation is to begin with a broad inter-

                             gated throughout the entire design to mini-          pretation of design, manufacturing and con-

                             mize repercussions for the realization of alter-     struction as it is today and propose a direction, 

                             nate design iterations.                              based on the natural development of organ-

                                                                                  isms, that could lead to a more effi cient way in 

                             This thesis begins with an investigation into        which to produce architectural works.  

                             Biomimicry as a new fi eld of study that is 

                             applicable to a wide variety of disciplines.  An     Based on the design methodology put forth in 

                             examination of key principles of natural design      the fi rst concept it will be possible to develop 

                             relevant to the focus of the thesis will create a    prototype design concepts that utilize the prin-

                             lens through which it will be possible to focus      ciples of natural design and construction.

                             on design and manufacturing techniques that 

                             are appropriate to biomimetic design.  A num-        This thesis does not deal with the cultural impli-

                             ber of questions related to current defi cien-       cations of what the formal physical appearance 

                             cies in  design and construction methodolo-          of a holistically designed architecture based on 

                             gies will be asked in an effort to generate a        biomimetic principles should be or what cul-

                             set of  answers that will aid in defi ning what      tural values it should refl ect.  Curvilinear archi-

                             objectives are to be met in the thesis and the       tectural forms are often referred to as being 

                             direction by which they will be attained.            organic or refl ective of organic design princi-

                                                                                  ples and as such, a cultural layer, vis a vis nature, 

                             The aim of this thesis is to develop an innova-      is applied to them. This thesis takes no position 

                             tive way in which to create curvilinear struc-       on the cultural signifi cance of curvilinear archi-

                             tural designs through a combination of the           tecture but focuses on this form of architec-

                             biomimetic principles of design that relate to       ture because it is believed that the biomimetic 

                             and inform the process of digital and para-          principles of design proposed in the thesis are 

                             metric design.  The desire, in its realization, is   a signifi cant improvement over current design 

                             to reduce the complexity of both design and          approaches to such forms of architecture.

                             construction in a manner that reduces the 

                                                                               4

## [p. 27]

1.1  Introduction to Biomimetics                   they relate to architecture are derived in part 

                                                                       from a long line of contributors within a vari-

                    While Buckminster Fuller is often attributed       ety of biological and architectural streams.

                    with the early incarnations, it is Janine Benyus, 

                    a science writer and lecturer on the environ-      From a historical standpoint the term biomi-

                    ment, who is responsible for the recent codi-      metics was introduced in the 1950s by Otto 

                    fi cation of Biomimicry as a fi eld of research    Schmitt, an American inventor, engineer and 

                    and study.  Her 1997 book entitled Biomimicry:     biophysicist who was responsible for devel-

                    Innovation Inspired by Nature brought together     oping the fi eld of biophysics and founding the 

                    the recent discoveries in a multitude of disci-    fi eld of biomedical engineering. 

                    plines, from engineering to agriculture, that can 

                    be traced to research and investigations into      Predating the work of Otto Schmitt is that of  

                    the designs and processes found in nature.  A      D’Arcy Thompson, an eminent biologist and 

                    number of propositions are put forth in the        mathematician who released his book entitled 

                    book that effectively illustrate the current       On Growth and Form in 1917.  This incredible 

                    trends and principles of Biomimetic investiga-     collection of work was instantly recognized 

                    tion.                                              for its originality and depth of scope.  Often 

                                                                       touted as “the fi rst biomathematician” it was 

                    1.  Nature as Model – Biomimicry is a science      Thompson who suggested that the infl uences 

                        that studies nature’s models and emulates      of physics and mechanics on the develop-

                        or takes inspiration from their designs and    ment of form and structure in organisms were 

                        processes to solve human problems.             underemphasized.  His book sought to illus-

                    2.  Nature as Measure – Biomimicry uses an         trate the connection between biological and 

                        ecological standard to judge the ‘rightness’   mechanical forms.  Thompson’s book does not 

                        of our innovations.  After 3.8 billion years   attempt to posit any type of discovery perva-

                        of evolution, nature has learned:  What        sive to all of biology, nor does he propose a 

                        works.  What is appropriate.  What lasts.      causal relationship between emerging forms in 

                    3. Nature as Mentor – Biomimicry is a holis-       engineering with similar forms in nature.  His 

                        tic way of viewing and valuing nature.  It     book presents a descriptive catalog of natu-

                        introduces an era based not on what we         ral forms and the mathematics that defi ne 

                        can extract from the natural world, but        them.  Since its release, the book has served 

                        on what we can learn from it.  (Benyus         as a wealth of inspiration for biologists, archi-

                        1997)                                          tects, artists and mathematicians.  (O’Connor 

                                                                       2006)

                    Although its formal introduction as a scientifi c 

                    discipline has been relatively recent, the prin-   “No organic forms exist save such are in con-

                    ciples and directives inherent in Biomimetics as   formity with physical and mathematical laws...

                                                                    5

## [p. 28]

The form, then, of any portion of matter,                 

                             whether it be living or dead, and the changes        Biomimetics goes further in that it strives to 

                             of form which are apparent in its movements          unify the knowledge contained within a diverse 

                             and in its growth, may in all cases be described     fi eld of scientifi c disciplines into one cohesive 

                             as due to the action of force.  In short, the form   unit.  This approach to design is seen as an 

                             of an object is a ‘diagram of forces’.”  (Thomp-     integrated network that is dependent upon 

                             son 1963, p11)                                       a feedback system related to the key factors 

                                                                                  in design.  These factors which comprise all of 

                             The following forms of architectural design          the relevant external and internal forces that 

                             vary with regard to their adherence to a strict      can infl uence a design from occupancy, load-

                             defi nition of biomimicry yet they all share a       ing, seismic, HVAC to daylighting inform the 

                             desire to derive architectural incentive from        direction of the design and interact with one 

                             nature.                                              another to create the fi nal solution.

                                                                                  ‘The attraction of Biomimetics for architects 

                             Organic Architecture – “…exalting the simple         is that it raises the prospect of closer integra-

                             laws of common sense—or of super-sense if            tion of form and function [with regard to a 

                             you prefer—determining form by way of the            holistic building design].  It promises to yield 

                             nature of materials...”  (Wright 1939)               new means by which buildings respond to, and 

                                                                                  interact with, their users - means more sub-

                             Evolutionary Architecture – “…an all-encom-          tle and more satisfying than present mechani-

                             passing applied philosophy based upon the            cal systems.  At a deeper level, according to 

                             profound study of nature’s processes, organ-         George Jeronimidis of the University of Read-

                             isms, structures and materials at a multitude of     ing, architects are drawn to the fi eld ‘because 

                             levels, from sub atomic particles to the kine-       we are all part of the same biology’.  The urge 

                             siology of insect and animal anatomy, to the         to build in closer sympathy with Nature is, he 

                             ecological relationships of living habitats, and     believes, a genuinely biological, and not merely 

                             then applies this knowledge to the design and        a Romantic, urge.’  (Aldersey-Williams 2003, 

                             construction of our built environment.”  (Tsui       p169)

                             2000) 

                                                                                  In this thesis, function is seen as co-evolving 

                             Anthroposophic Architecture – “…which  with the development of form in that each 

                             seeks to respond to the human form and               exert an infl uence on one another.  A desired 

                             human needs [where] buildings should appear          shape (form) may be created and a structural 

                             in harmony with the landscape in which they          system (function) derived from it, however, 

                             are built, with regard to both form and mate-        the requirements of the structural system may 

                             rial.”  (Pearson 2001, p5)                           infl uence and require subsequent changes in 

                                                                               6

## [p. 29]

the form.   A feedback exists between form 

                    and function where the varying conforma-

                    tional possibilities of a design will lead to 

                    unique structural adaptations specifi c to that 

                    form. 

                    The appeal of biomimetics stems not merely 

                    from a method for acquiring abstract design 

                    ideas from nature but also from the manner 

                    in which nature utilizes those ideas.  Common 

                    to both natural and man-made environments 

                    is the issue of cost.  There is always an issue 

                    of how much an object, structure, or organ-         1.  Map of biomimetic processes.  

                    ism will cost to design, manufacture, construct, 

                    maintain and ultimately recycle.  In an architec-

                    tural sense this can be reduced to a monetary 

                    cost where often times the lowest tender wins.      not always translate from one to another in an 

                    In the natural world the cost is energy, where      effi cient manner.  Thus, a concept will become 

                    competition for available resources favors the      much more robust if we are able to distill 

                    organism that can survive and grow with the         innovative design and manufacturing inspira-

                    least amount of required materials and energy       tion (with regard to the current manufacturing 

                    expenditure.  Animals must fi ght for territory,    techniques available) from natural phenomena 

                    sex, and food while plants develop innova-          rather than strictly attempting to mimic them.  

                    tive ways to harness more sunlight than their       (Vincent 2002, p4)  See Figure 1.

                    neighbors.  In simple terms it can be proposed 

                    that the organism which survives best is the        1.2     Direct Approach to Biomimetic   

                    one that produces more viable offspring per                 Investigation

                    unit of expended energy than its competitors.  

                    Similarly, an architect must balance a number of    A direct method of investigation actively seeks 

                    design variables that equate to the investment      to defi ne the nature of the design problem 

                    of cost which may be structure, appearance,         and the context of its creation and use.  With 

                    effi ciency, or any other number of require-        a clear understanding of the design require-

                    ments.  The design that offers the best product     ments it is then possible to look to the natural 

                    for the least amount of investment will often       world for examples that fulfi ll them.  It is useful 

                    be the one that is produced.  It is worth noting    to investigate an array of divergent organisms 

                    however that the design capabilities, materials,    that rely on different approaches to solve simi-

                    manufacturing and construction methods we 

                    as designers have in our palette are different      lar problems.  This will yield a greater variety of 

                    from those found in nature, and as such do          ideas with which to develop.  Structural solu-

                                                                        tions, for example, do not rest solely in mam-

                                                                     7

## [p. 30]

malian bone but can be found in the compo-        4.  The Power of Shape – Nature uses many 

                            sition of wood, the shell of an arthropod, the         structurally effi cient non-orthogonal forms 

                            exoskeleton of an insect or in an individual           with which to create its structures.    

                            plant leaf.  Unique solutions can develop from     

                            a wide variety of inspirations.                   5.    Materials as Systems – Nature builds from 

                                                                                   small to large with a corresponding scaling 

                            1.3     Indirect Approach to Biomimetic                of function in relation to the materials and 

                                    Investigation                                  components involved for particular func-

                                                                                   tions.

                            An indirect method of investigation seeks to 

                            fi nd solutions through defi ning the general     6.   Natural selection as an innovative engine 

                            principles of natural design and using those           – Environmental forces that act on an 

                            as guidelines for developmental progression.           organism and affect its fi tness will direct 

                            While it is diffi cult to effectively categorize       the development of future organisms.

                            the entire collection of natural designs into 

                            discrete units there arise recurring principles,  7. Material Recycling – Create structures 

                            as described below, that have been observed            using materials that are non-toxic and can 

                            which form a coherent strategy for investiga-          be fully recycled at the end of their life. 

                            tion. 

                                                                              8.  Ecosystems that Grow Food – Systems 

                            12 Methods by Which Nature Can Inform                  are created that have a net surplus of pro-

                            the Development of Technology:  (Benyus                duction without a corresponding draw-

                            2004)                                                  down of environmental resources.

                               

                            1.  Self Assembly – The ability of an organism    9.  Energy savvy movement and transport 

                                to direct its own process of development.          – Locomotion and internal circulation sys-

                                                                                   tems have adapted to require a minimal 

                            2.  Chemistry in Water – Nature produces               investment of energy for their purpose.

                                all of its compounds in normal environ-

                                mental conditions without a necessity for     10.  Resilience and Healing – Living organisms 

                                extreme temperatures or harsh chemi-               have the ability to absorb and rebound 

                                cals.                                              from impacts and can repair themselves if 

                                                                                   damage is incurred.

                            3.  Solar Transformations – Many organisms 

                                respond actively to the sun to maximize       11. Sensing and Responding – A series of 

                                their energy absorption.                           feedback systems within an organism 

                                                                                   allow it to sense a variety of environmen-

                                                                            8

## [p. 31]

tal factors acting on it and to respond to 

                         these in a suitable manner.

                    12. Life creates conditions conducive to life 

                         – The waste products and various by-

                         products of growth and sustenance create 

                         materials that are benefi cial to the growth 

                         of other organisms.

                    1.4      Biomimetic Solutions in Other 

                             Design Disciplines:

                    Man-made designs throughout history have 

                    been realized through observations and inves-

                    tigations into the natural world, albeit on vary-

                    ing degrees from imitation to inspiration.  From 

                    the creations of Leonardo DaVinci, including 

                    his fl ying wing, to the present day work with 

                    nanotechnology, a variety of disciplines have 

                    realized the potential source of design inspira-

                    tion that nature has.  The following examples 

                    provide a brief list of areas where biomimetic 

                    infl uences can be found.  (Vogel 1998, p276-

                    279)

                    1. Streamlined bodies – The study of aquatic 

                         organisms led to advances in the develop-

                         ment of streamlined shapes in technology.  

                         Like the trout or dolphin a body that trav-

                         els through the air or water experiences 

                         least resistance if it is rounded in the front 

                         and tapers to a rear point.

                    2. Airfoils – Bird wings have curved tops and 

                         fl atter bottoms.  This aerodynamic shape is 

                         essential to provide lift for aircraft wings.   2.  Rounded pleats of automobile air fi lter inspired from  

                                                                             a dolphin’s nose.

                                                                         3.  Pultrusion machine for carbon fi ber.

                                                                         4.  High magnifi cation of Velcro hooks.

                                                                      9

## [p. 32]

3. Maneuverability of Aircraft – Upon 

             observing the fl ight of buzzards the Wright 

             Brothers determined that they regain their 

             lateral balance when partially overturned 

             by a gust of wind by torsion of the tips of 

             their wings.  This discovery prompted the 

             development of ailerons that control the 

             banking movement of the airplane which 

             cause it to turn.

           4. Extruded fi bers – Silkworms and spiders.  

             Extruded fi bers such as carbon fi ber are 

             developed from the principles learned 

             from these creatures.  While the process 

             of formation is not identical the theory 

             behind the technology was established 

             through their investigation.

           5. Telephone transducers – Emulations of 

             the components in an eardrum.

           6. Velcro – Examination of the barbs on bur-

             dock burs.

           7. Drag reduction – Fish slime and their use 

             of long, linear, soluble polymers.

           8. Peristaltic pumps – The intestines of many 

             organisms move fl uids through peristal-

             tic action.  In industry, peristaltic pumps 

             use rotating rollers pressed against spe-

             cial fl exible tubing to create a pressurized 

             fl ow.  The tube is compressed at a num-

             ber of points in contact with the rollers 

             or shoes.  The media is moved through 

             the tube with each rotating motion.  Mov-

             ing parts do not come in contact with the 

                              10

## [p. 33]

2.0     Exploration of Biomimetic 

                             Design Principles

                     The natural world does not consciously organize itself based 

                     on singular and separate approaches to solve the twelve 

                     methods of design outlined in Section 1.2.  Rather, its designs 

                     develop through an interdependency of each design method 

                     to arrive at a fi nal product.  While this approach would be 

                     ideal in the creation of man-made designs we must fi rst delve 

                     into the unique characteristics and contribution to design 

                     that each holds before we can endeavor to formulate an effi -

                     cient solution that encompasses them.  The desired outcome 

                     for this thesis, being the development of a more effi cient and 

                     streamlined overall approach to design and construction and 

                     specifi cally the use of natural design in the creation of non-

                     orthogonal structurally supportive building skins, relies on 

                                                 Section 1.2.  

                     a selection of fi ve designs methods outlined in 

                     The following subset of imperatives were chosen for their 

                     relevance to structure and design process at it relates to the 

                     development of the thesis.  It should be noted however, that 

                     the further development of the thesis outcome need not be 

                     limited strictly to a subset of the design methods but could 

                     with further research grow to encompass all of them.

                                11

## [p. 34]

2.1     Self Assembly:                                 an organism must be derived from a relatively 

                                                                                     unresolved set of plans.  (Vogel 1998, p25)

                              2.1.1  DNA and Genetic Coding:

                                                                                     ‘To a remarkable extent the dazzling diversity 

                              ‘Theoreticians fi ercely contest the precise rela-     in nature represents superfi cial features of sys-

                              tionship of morphogenesis to genetic coding,           tems of an exceedingly conservative and ste-

                              but there is an argument that it is not the form       reotypical character’  (Vogel 1998, p31)

                              of the organism that is genetically encoded but 

                              rather the process of self-generation of the           The relative lack of information clearly under-

                              form within an environment.  Geometry has a            lies a lot of biological design.  In 1950 an emi-

                              subtle role in morphogenesis.  It is necessary to      nent physicist, Horace R. Crane, predicted that 

                              think of the geometry of a biological or com-          many subcellular structures would turn out to 

                              putational form not only as the description of         be helical in form, not because helices neces-

                              the fully developed form, but also the set of          sarily worked best but because they could be 

                              boundary constraints that act as a local orga-         assembled with especially simple instructions.  

                              nizing principle in the self-organization during       Crane anticipated not only the double helix of 

                              morphogenesis.’  (Weinstock 2004, p14)                 DNA but its supercoiling, the so called alpha 

                                                                                     helix of parts of many proteins, and, on a larger 

                              Nature has adapted the plans from which it             scale, helical microtubules and microfi laments 

                              derives organisms to be based on a relatively          important in maintaining the shape and motil-

                              simple set of instructions.  The fertilized egg of     ity of cells.  Microtubules and microfi laments 

                              a human or similar animal has approximately            have a remarkable capacity for self-assembly; if 

                                 10                                                  all the components are put together (with per-

                              10  bits of information in its DNA that are 

                              responsible for the plan of the organism.  A           haps a bit of the formed structure as a starter) 

                              human is composed of around 1014 cells which           they ordinarily fall into place without any need 

                              is a magnitude of 10,000 times greater than the        for mold of scaffolding or, more important, for 

                              number of instructions contained within the            any additional information.  (Vogel 1998, p26)

                              egg.  With the onset of computer aided design 

                              and 3D modeling we have come to realize                Building large organisms out of many cells is 

                              that with every additional layer of complex-           probably made necessary by that shortage of 

                              ity we introduce into a model there is a cor-          information.  Cells may look diverse, but they 

                              responding increase in fi le size and processing       all have a lot in common; if you can build one 

                              time.  Organisms in the same way are three-            kind, you need only a little more information, 

                              dimensional and as a result should require a           relatively speaking, to build all the others.  Fur-

                              vastly greater amount of information for mor-          thermore, in the development of each indi-

                              phogenesis to take place than is available in the      vidual, one group of instructions can set more 

                              cell.  From this it can be said that the form of       than one structure.  In humans, hand size is 

                                                                                 12

## [p. 35]

an excellent predictor of foot size.  Bilateral    2.1.3 Molecular self-assembly:

                    symmetry is an effi cient method by which the 

                    number of instructions required to derive a        Molecular self-assembly is the assembly of 

                    developed form is essentially halved.  A single    molecules without guidance or management 

                    alteration of the genetic material – a muta-       from an outside source. There are two types of 

                    tion – ordinarily affects both sides of the body   self-assembly, intramolecular self-assembly and 

                    of an animal.  The heart and lungs of all of us    intermolecular self-assembly.  Intramolecular 

                    are in the same position but at some level of      self-assembling molecules are often complex 

                    detail the locations of our parts are unpredict-   polymers (primary structure) with the ability 

                    able.  Anatomy students learn the names of         to assemble from the random coil conforma-

                    the large blood vessels, but the small ones stay   tion into a well-defi ned stable structure (sec-

                    anonymous – simply because their arrange-          ondary and tertiary structure).  An example of 

                    ment varies from one person to the next.           intramolecular self-assembly is protein folding. 

                    (Vogel 1998, p27)                                  Intermolecular self-assembly is the ability of 

                                                                       molecules to form supramolecular assemblies 

                    2.1.2   Self Assembly in Nature:                   (quaternary structure).

                    Nature uses the process of self-assembly as        Self-assembly can occur spontaneously in 

                    the fundamental principle which generates          nature, for example in cells (such as the self-

                    structural organization on all scales from mol-    assembly of the lipid bilayer membrane) and 

                    ecules to galaxies.  It is defi ned as a process   other biological systems.  See Figure 5.  It 

                    whereby pre-existing parts or disordered  results in the increase in internal organization 

                    components of a pre-existing system form           of the system.  Many biological systems use 

                    structures of patterns.  Self-assembly can be      self-assembly to assemble various molecules 

                    classifi ed as either static or dynamic.  Static   and structures. Imitating these strategies and 

                    self-assembly is an ordered state that occurs      creating novel molecules with the ability to 

                    when the system is in equilibrium and does         self-assemble into supramolecular assemblies 

                    not dissipate energy.  Dynamic self-assembly       is an important technique in nanotechnology.  

                    is when the ordered state requires dissipation     (Whitesides 2002, p2418-21)

                    of energy.  Examples of self-assembling system        

                    include weather patterns, solar systems, histo-    2.1.4 Structural Development

                    genesis (the formation and development of tis-

                    sues) and self-assembled monolayers (mono-         Patterns – “The interest in patterns is pri-

                    molecular fi lms).                                 mary in that they are essential to the struc-

                                                                       tural framework of natural and artifi cial sys-

                                                                       tems.  We can no longer reduce things to sin-

                                                                       gular elements but instead see that everything 

                                                                   13

## [p. 36]

is made up of a series of interrelated parts that 

                                                                                                     perform together as a collective whole.  From 

                                                                                                     the cellular structure of living organisms to the 

                                                                                                     networks that make up our connected soci-

                                                                                                     ety, patterns are always the agents that allow 

                                                                                                     the total assembly to evolve and adapt to a 

                                                                                                     changing environment…  Traditionally, struc-

                                                                                                     tural patterns are defi ned in Cartesian space 

                                    5.  Self assembly of inorganic nanoclusters.                     and require prescribed repetition and a high 

                                                                                                     degree of redundancy for structural integrity.  

                                                                                                     By pursuing a reconfi guration of component 

                                                                                                     relationships which reveal themselves in design 

                                                                                                     solutions, forces are dissipated through a sys-

                                                                                                     tem in multiple directions and transferred to 

                                                                                                     the substructures.  Structurally patterned mod-

                                                                                                     ularity is deployed at different scales, in various 

                                                                                                     confi gurations, with adjustable degrees of den-

                                                                                                     sity and directionality.  See Figure 6.  Specifi cally, 

                                                                                                     it is now possible to see the joint, or point of 

                                                                                                     intersection as a more dynamic aspect in the 

                                                                                                     tectonic defi nition.  No longer bound by iden-

                                                                                                     tical repetition, the joint must now be capa-

                                                                                                     ble of providing iterative difference if it is to 

                                    6.  Process illustrating the evolution from path to              respond to the surface transformations result-

                                    surface, and pattern to structure.                               ing from the structural and ornamental inter-

                                                                                                     play.” (Bell 2004)   See Figure 7. 

                                                                                                     Essentially, the system of a structural hierarchy 

                                                                                                     based on the gradual reduction of individually 

                                                                                                     separate components that is favored today is 

                                                                                                     reinterpreted so that the boundaries between 

                                                                                                     successive structural layers is blurred and the 

                                                                                                     building becomes one indivisible unit from the 

                                                                                                     micro to macro scale.  This approach reduces 

                                                                                                     the vulnerability of a building to failure due 

                                                                                                     to localized stresses, as the structural system 

                                    7.  Structural analysis of shell comprised of radial and         has built in structural redundancy acting on a 

                                    random patterns. 

                                                                                                 14

## [p. 37]

number of levels to dissipate localized stresses 

                    throughout the entire structure.  The pattern-

                    ing that takes place in this method can occur 

                    in a variety of confi gurations from a simple 

                    scaled grid shaped layout to a more complex 

                    fractal geometry whose forms are identical at 

                    a number of scales.

                    2.1.5    Endoskeletons and Exoskeletons:

                    Terrestrial organisms must exist in an environ-

                    ment subject to both gravity and atmospheric 

                    pressure.  Aquatic organisms deal with gravity, 

                    although to a lesser extent, as well as water 

                    pressure.  In order to counteract the forces 

                    acting within and on them as well to main-

                    tain their form and possible requirement for 

                    locomotion and morphological fl uidity, organ-

                    isms must utilize a structural organization that 

                    can accommodate the same.  The structural 

                    system used by the majority of multi-cellular 

                    organisms can be classifi ed as belonging to 

                    one of two types:

                    1.  Endoskeletons (Internal Structure) - Ani-

                    mals with endoskeletons can grow easily 

                    because there are no rigid outside boundaries 

                    to their bodies. They are vulnerable to wound-

                    ing from the outside, but repair of the living tis-

                    sue is usually not a problem.   See Figure 8.

                    2.  Exoskeletons (External Structure) - Exo-

                    skeletons are outside the body and encase it 

                    like armor. They are light and very strong, and 

                    provide attachment places for the muscles 

                    inside. They protect the body from dehydra-

                    tion, predators, and excessive sunlight.  See Fig-    8.  Human Endoskeleton,

                    ure 9.      

                                                                      15

## [p. 38]

2.2     The Power of Shape:

                                                                                             2.2.1     Fundamentals of Natural Form

                                                                                             Nature utilizes a variety of forms and design 

                                                                                             methods in its constructions to ensure maxi-

                                                                                             mization in terms of structural effi ciency and 

                                                                                             mobility while minimizing the required input 

                                                                                             of material.  

                                                                                             1.    Maximize structural strength – Nature 

                                                                                             employs a relatively small amount of materials 

                                                                                             in its assemblies as compared to human con-

                                                                                             structions.  However, through unique confi gu-

                                                                                             rations of these simple materials nature is able 

                                 9.  Crab Exoskeleton.                                       to create structures that outperform many 

                                                                                             man-made structures.  (Tsui 1998)

                                                                                             2.    Maximize  enclosed  volume – In order 

                                              Sphere                                         to conserve heat organisms must maintain an 

           Surface Area (x2)2336475766effi cient balance between their surface area 

           Volume (x3) 1020304050and internal volume.  Through the use of cur-

                                                                                             vilinear forms nature is able to maximize the 

                                               Cube                                          internal volume of an organism while minimiz-

           Surface Area (x2)2844587081

           Volume (x3) 1020304050ing its surface area.  See Figure 10.  This has 

                                                                                             the effect of reducing the amount of heat lost 

                                 10.  Surface Area and Volume Correlation for Sphere         across the surface of an organism to a mini-

                                 and Cube.                                                   mum, thus allowing it to remain warmer with 

                                                                                             less input of energy.  Additionally, a smaller sur-

                                                                                             face area results in a requirement for less input 

                                                                                             of materials to form the organism as well as a 

                                                                                             reduction in weight.  (Tsui 1998)

                                                                                             3.  Create high strength-to-weight ratios 

                                                                                             – Since there is competition for material 

                                                                                             resources within an ecosystem, natural organ-

                                                                                             isms must utilizes unique methods of con-

                                                                                         16

## [p. 39]

struction that minimize the input of material 

                   and expenditure of energy while maximizing 

                   the subsequent strength achieved.  Bones in 

                   an organism vary their cross section over their 

                   length to deposit material where it is most 

                   needed.  In addition, cross-linking of the fi bers 

                   in the bone contribute to strength increases 

                   without a corresponding increase in weight.    

                   (Tsui 1998) See Figure 11.                       11.  Cross-section of Bird Bone. 

                   4.    Use stress and strain as a basis for struc-

                   tural effi ciency – Natural forms are derived 

                   from their varying rates of growth and these 

                   three dimensional shapes are dependent on 

                   an irregular rate of growth throughout the 

                   organism.  The external environment exerts 

                   stresses on the developing object and its result-

                   ing form is a product of its response to the 

                   environment and the limits of the structural 

                   properties of the material used.  This process 

                   occurs on both short and long term scales of 

                   time where evolution has contributed to the 

                   genetic code that defi nes the growth template 

                   while stresses acting on an within the organ-

                   ism shape the fi nal and ongoing form.  (Tsui 

                   1998)

                   5.  Integrate aerodynamic effi ciency  with 

                   structural form – Many organisms are mobile 

                   and as such are subjected to the laws of aero-

                   dynamics or hydrodynamics.  To effectively 

                   inhabit their environment the form of the 

                   organism is often tailored to maximum effi -

                   ciency for the minimal expenditure of energy 

                   for locomotion or resistance to environmen-      12.  Effects of Wind and Live Load on Structure.  

                   tal stresses such as wind on a tree.  Similarly, 

                   a curved wall is able to more easily dissipate 

                                                                 17

## [p. 40]

wind load as well as requiring less material in 

                                                                                   order to do so.  (Tsui 1998)  See Figure 12.

                                                                                   6.   Curvilinear forms that disperse and dis-

                                                                                   sipate multidirectional forces – Through the 

                                                                                   use of curvilinear forms, organisms have the 

                                                                                   ability to absorb and dissipate loads throughout 

                                                                                   their structure which helps to reduces areas of 

                                                                                   collected stress and the need for unnecessary 

                                                                                   structural reinforcement.  (Tsui 1998)  See Fig-

                                                                                   ure 13.

                                                                                   2.2.2    Forms that Organisms in Nature  

                                                                                            are Composed of:

                                                                                   The natural world contains a wide array of 

                                                                                   organisms that are composed of many differ-

                                                                                   ent forms and shapes.  The variety of intricate 

                                                                                   forms however, can be thought of as belong-

                                                                                   ing to a set of basic shapes and structures with 

                                                                                   each organism using them in different propor-

                                                                                   tions.  (Tsui 1999, p86-131).  See Figures 14-

                                                                                   19.

                                                                                   1.   Curved shells – Skulls, eggs, exoskeletons 

                             13.  Effects of Live Load on Structure.               (domed roofs)

                                                                                   2.   Columns – Tree trunks, long bones, endo-

                                                                                   skeletons (posts)

                                                                                   3.   Stones embedded in matrices – Worm 

                                                                                   tubes (concrete)

                                                                                   4.   Corrugated  structures – Scallop shells, 

                                                                                   cactus plants, stiffness without mass (doors, 

                                                                                   packing boxes, aircraft fl oors, roofs)

                                                                                   5.   Spirals – Sunfl owers, shells, horns of 

                                                                                   wild sheep, claws of the canary bird (domed 

                                                                                   roofs)

                                                                                   6.   Parabolic Forms – Tardigrade (pneumatic 

                                                                                   structures)

                                                                               18

## [p. 41]

2.2.3    Forms of Structures that Organisms  

                          Build:

                    Many organisms fashion their shelters out of 

                    natural material located within their own habi-

                    tat.  Whether produced from found material 

                    or as a result of internal production, as with 

                    spiders, the variety of forms that organisms 

                    construct can also be categorized into a set 

                    of recurring forms and principles.  (Tsui 1998) 

                    See Figures 21-25.

                    1.   Combined structural shapes and forms 

                    – Termite towers, prairie dog burrows

                    2.   Parabolic Forms – Bowerbird nests

                    3.   Hemisphere/mound  forms – Beaver 

                                                                          From top left.  14.  Human skull.  15.  Human femur.  16.  Scallop shell.  17.  Snail shell.  

                                                                          18.  Tardigrade.  19.  Sunfl ower, shell.  

                                                                      19

## [p. 42]

dams, ant nests, 

                                     4.   Tension/membrane structures – Leaf cut-

                                     ter ant nest, weaver ant nest, silkworms, spider 

                                     webs

                                     5.   Hemisphere/sphere – Potter wasp, oven-

                                     bird nest, cactus wren nest, spittlebug nest

                                     6.   Egg/bell  shapes – Africa gray tree frog, 

                                     paper wasp and honeybee nest, weaverbird 

                                     nest

                                     7.   Tube/cylinder  forms – Swallow tailed 

                                     swift nest, bagworm case, jawfi sh, shark and 

                                     the helix, brine shrimp nest

                                     2.2.4 Flatness:

                                     Advantages of being fl at:

                                     1.  Easy to walk on at any point - An even 

                                       fl oor, void of surface deformation, allows 

                                       ease of circulation at any area on the sur-

                                       face 

                                     2.   Utility in a world dominated by gravity - 

                                       Gravity allows for rapid construction with 

                                       regard to the creation of level surfaces as 

                                       well as in material application where con-

                                       crete, for example, has the tendency to 

                                       level itself based on gravity.;

                                     3.   Wall of minimal area that separates two 

                                       compartments - A straight wall between 

                                       adjoining rooms or buildings has the least 

                                       amount of area requiring surfacing.  

                                     Clockwise from top left.  21.  Spittlebug cocoon.  22.  

                                     Ant nest.  23.  Weaverbird nest.  24.  Spiderweb.  25.  

                                     Termite tower.

                                    20

## [p. 43]

4.   Materials pile smoothly on one another        rise buildings weight is a major factor in 

                      -  Flat and straight materials are effi cient  design and the desire is to reduce the 

                      because they allow for a regular and max-      loading that occurs cumulatively on the 

                      imized arrangement during transport            supporting members.  A small increase in 

                      to the site and subsequent storage until       weight on the top fl oors and roof of a 

                      ready for use.   In terms of construction,     building will result in a signifi cant increase 

                                                                     in loading that the structural members of 

                      fl at roofs are easy to build and handy to     the lower fl oors of the building must sup-

                      use.  Beams and boards can be laid parallel    port.  This results in additional material 

                      on top of each other for ease of transpor-     and building costs.

                      tation.  Shingling becomes a strictly two-

                      dimensional operation.  Simple instruc-     4.   Longer means weaker - With the require-

                      tions are required for their assembly.         ment for minimal surface defl ection to 

                                                                     prevent cracks from developing on sur-

                  Disadvantages of being fl at:                      face fi nishes as well as to prevent fl ex 

                                                                     from occurring a beam must meet the 

                  1.  Sag at the center of a horizontal ele-         structural requirements imposed on it.  

                      ment – Depending on the size and span          A longer beam will defl ect more and be 

                      requirements of building elements a cer-       able to resist less loading than a shorter 

                      tain amount of gravitational sag will occur    one.  As a result, an increase in span will 

                      due both to dead and live loading.  To pre-    require either an increase its beam depth 

                      vent sag from occurring, a large amount of     or decrease the column to column dis-

                      material may be required to provide ade-       tance.  Both have the effect of increasing 

                      quate fl exural resistance.                    material weight and costs.

                  2.   The greater the loading the thicker must 

                      be the fl oor or the horizontal beams 

                      that support it - When the requirement 

                      for loading increases in a typical slab and 

                      beam scenario it is necessary to increase 

                      the depth of either one or both to attain 

                      the required strength.  This will result in 

                      greater fl oor to fl oor heights and subse-

                      quent material costs or reduced ceiling 

                      heights.   

                  3.  Exacts a considerable price paid with 

                      regard to weight - In fl at roofs and high 

                                                                  26.  Plant leaf.  27.  Dragonfl y wing.  28.  Cactus.  

                                                              21

## [p. 44]

How nature deals with fl atness:

                                                                                                      1.   Veins -  Veins increase the functional thick-

                                                                                                            ness of leaves with only a little extra invest-

                                                                                                            ment of material.  See Figure 26 & 27.

                                                                                                      2.   Curvature - Without the need for veins, 

                                                                                                            a fl at surface can be effectively thickened 

                                                                                                            and stiffened with the introduction of a 

                                                                                                            small amount of curvature.

                                    29.  Surface Tension in Cylindrical and Spherical Vessels.        3.   Pleats - The introduction of a set of pleats 

                                                                                                            running in the direction in which bending 

                                                                                                            is expected increases the effective thick-

                                                                                                            ness without going to the trouble of add-

                                                                                                            ing proper beams beneath the surface.  

                                                                                                            See Figure 28.

                                                                                                      The wings of an insect comprise only 1% of 

                                                                                                      their body mass.  Their structural integrity 

                                                                                                      is derived from a combination of curvature, 

                                                                                                      veins and lengthwise pleats.  The key here is 

                                    30.  Relationship between radius and tension.                     the fact that nature, as seen with the insect 

                                                                                                      wing, often combines all three of these meth-

                                                                                                      ods which can multiply their effects.

                                                                                                      Automotive manufacturers discovered the 

                                                                                                      benefi ts of curvature when the unibody 

                                                                                                      replaced the traditional ladder frame.  Pressing 

                                                                                                      a piece of metal into a curved shape is much 

                                                                                                      simpler and uses less material than spot weld-

                                                                                                      ing stiffener plates to achieve strength.  Essen-

                                                                                                      tially the central spine of the automobile was 

                                                                                                      removed and replaced by a structural skin.  

                                                                                                      (Vogel 1998, p57-60)

                                                                                                  22

## [p. 45]

_(página sin capa de texto)_

## [p. 46]

angles except in bacteria and certain pro-

                                                                                            tozoa and foraminifera.  Round houses usu-

                                                                                            ally indicate a nomadic/semi-nomadic society 

                                                                                            where curvilinear buildings are more econom-

                                                                                            ical of material, less weight and easier to erect.  

                                                                                            Rectangular houses typify sedentary societies 

                                                                                            where it is possible to include more buildings 

                                                                                            in a specifi ed area, the interiors can be parti-

                                                                                            tioned more easily and subsequent additions 

                                                                                            become easier as well.

                                                                                            Corners and Cracks – Humans tend to prefer 

                                                                                            sharp corners while nature uses rounded cor-

                                                                                            ners.   See Figures 31 & 32.  There are a num-

                                                                                            ber of reasons why sharp corners are inef-

                                 34.  World Trade Towers.                                   fi cient and impractical.  We still prefer them 

                                                                                            for ease of construction, however.  Cracks in 

                                                                                            a structure originate where the stresses are 

                                                                                            the greatest and this happens to take place in 

                                                                                            the corner of structures.  See Figure 33.  The 

                                                                                            problem is intensifi ed when two materials are 

                                                                                            brought together by means of a fastener.  The 

                                                                                            fastener is thus entrusted with handling both 

                                                                                            attachment of the materials and the resulting 

                                                                                            forces that are acting upon them.  The rele-

                                                                                            vance of this structural reality has been well 

                                                                                            recognized in other realms of construction 

                                                                                            and has been dealt with in an effort to pre-

                                                                                            vent structural failure.  Airplanes and ships 

                                                                                            must both deal with an enormous amount 

                                                                                            of stress throughout their fuselages and hulls 

                                 35.  Tree in hurricane conditions.                         without breaking apart.  On the large scale the 

                                                                                            shape of their form is predominantly curvilin-

                                                                                            ear so as to distribute forces evenly.  The win-

                                                                                            dows and portholes in each are also rounded 

                                                                                            to prevent crack propagation.  This method of 

                                                                                            stress distribution and dissipation has been in 

                                                                                        24

## [p. 47]

use for millennia in many of nature’s organisms,        response to the same uneven loading that can 

                      from the bones in our bodies to the forking of          prove disastrous for stiff structures.

                      a branch in every tree.

                                                                              2.2.8    Increases in Scale:

                      2.2.7    Stiffness and Flexibility:

                                                                              Size – When objects grow in size their volume 

                      Stiffness – Predominates in architectural con-          increases more drastically than does their sur-

                      struction while nature prefers strong, fl exible        face area.  This can have a profound effect on 

                      structures.  Stiff materials like bricks and blocks     the ability of the object to resist and respond 

                      are quite plentiful, easy to assemble and work          to the internal and external forces acting on 

                      quite well in compression but are quite sus-            it for which it was originally designed.  Simply 

                      ceptible to failure due to accidents or unusual         scaling the size of an object does not necessar-

                      loading.  See Figure 34.  Most suffi ciently stiff      ily mean that a corresponding increase in the 

                      structures are strong enough to resist collapse,        magnitude of its structural components will 

                      however an adequately strong structure is not           prove adequate for structural integrity

                      necessarily suffi ciently stiff enough for occu-

                      pancy comfort.  In the search for our desired           Heat – Heat is generated throughout an ani-

                      stiffness there is a proportionate increase in          mal’s insides but lost across its surface.  One 

                      material that must accompany it.  The stiffness         large and one small animal produce heat at 

                      encountered in natural products like bone,              the same rate.  The larger volume rich, sur-

                      ceramics, coral and mollusks are made from              face poor animal would be warmer.  Keeping a 

                      compounds that exist abundantly in nature               large building heated is cheaper, relative to its 

                      yet these compounds are used only in crucial            volume than is a small house.

                      locations rather than throughout the organism 

                      where other fl exible materials may be substi-          Columns – A structure may fail to support its 

                      tuted and possibly required.                            load if a member in compression buckles, that 

                                                                              is, moves laterally and shortens under a load it 

                      Flexibility – With exception of the strategic           can no longer support. The critical force var-

                      use of stiff materials, the majority of an organ-       ies with the fourth of the column’s diameter 

                      ism is constructed with relatively fl exible mate-      divided by the square of the column’s height.  

                      rials.  From an architectural standpoint, fl ex-        Therefore, a column with a twofold increase 

                      ible materials are benefi cial in that they can         in size (diameter and height) will experience 

                      withstand extreme external conditions like              a fourfold increase in resistance to buckling.  

                      the impacts of waves, wind and earthquakes              However, being consistent with the properties 

                      without failing because they are able to fl ex          of linear versus volumetric increases we end up 

                      and absorb their energy.  See Figure 35.  Flex-         increasing the weight of both the column and 

                      ibility allows a structure to alter its shape in        whatever it loads eight times.  This results in a 

                                                                          25

## [p. 48]

scenario where the dead load becomes twice             2.4      Materials as Systems:

                              what the column can support thus resulting in 

                              failure.  As the scale of a building increases, it     Organisms and natural systems are often 

                              is possible to see that there is a four-fold rela-     times composed of a number of interrelated 

                              tionship between the mass of the building and          components and materials that act on a con-

                              the structure required to support it.  A small         tinuous scale from the micro to macro struc-

                              increase in the size of a building will result in a    ture.  At each level of structural organization 

                              relatively large increase in the required build-       the cells within the organism perform a func-

                              ing materials.                                         tion that corresponds to a necessary require-

                                                                                     ment at that level.  

                              2.3     Resilience and Healing: 

                                                                                     The cells within a tree perform this hierarchy of 

                              If an organism is subjected to an external force       functions at different scales.  At the micro level 

                              that causes damage a number of conditions              the cells are responsible for the movement of 

                              must be met.  First of all it must be resilient        water from the roots to the leaves.  Based on 

                              to the force or impact so as to reduce the             weight, the tubular structures of the cells are 

                              initial damage experienced.  This means utiliz-        also stronger than a solid structure that would 

                              ing a structural system that contains within it        not be able to act as a transport mechanism.  

                              a redundancy of structure that distributes the         When these cells are grouped together they 

                              force of impact and prevents a catastrophic            provide the tree with a high strength light-

                              structural failure.  Subsequent to the damage          weight structural system that resists both ten-

                              the organism must be able to repair itself with-       sile and compressive forces as well as allowing 

                              out a corresponding loss of function.                  for fl exibility.  See Figures 36 & 37.

                                                                                     2.5     Sensing and Responding:  

                                                                                     2.5.1    Static and Dynamic Structures

                                                                                     To exist and maintain itself throughout its life, 

                                                                                     an organism must possess the ability to both 

                                                                                     sense the external environmental forces acting 

                                                                                     on it and respond to these forces in a way that 

                                                                                     minimizes damage and eliminates the need for 

                              36.  Cross-section of Douglas Fir Cells.               an investment of unnecessary material and 

                              37.  Cross section of vascular bundle in wood (xylem   structural reinforcement.  The ability of biologi-

                              cells visible).                                        cal organisms and structures to function in this 

                                                                                     regard can be categorized into two systems 

                                                                                     that are of interest.  

                                                                                 26

## [p. 49]

1.  A closed loop system - The structure has 

                   an integrated dynamic ability to sense one or 

                   more variables (strain, temperature, etc.), pro-

                   cess the variable, and act, sense, and reprocess 

                   to continue the performance required of the 

                   design.

                   Living bone is a material that is in a constant 

                   state of reformation to accommodate the 

                   changes in its loading.  While these changes 

                   may occur over the course of many months, 

                   the cycle can begin within minutes of an exter-

                   nal action.                                        38.  Cross-section of shell matrix.  

                                                                      39.  Detail of shell mollusk microstructure. 

                   Unlike the relatively slow and continuous pro-     2.5.2   Natural Development of Form:

                   cess that bone undergoes, the leaves of a tree 

                   are able to realign and reconfi gure themselves    Natural forms are derived from their vary-

                   with quick deformation in response to wind.        ing rates of growth and these three dimen-

                                                                      sional shapes are dependent on an irregular 

                   2.  An open loop system - This principle of        rate of growth throughout the organism.  The 

                   design is aimed at enhancing toughness, which      form reached at the end of the growth cycle 

                   leads to a mechanical integrity of the system.     is determined both by the physical limitations 

                   There is no feedback mechanism but the static      of the construction material and its differential 

                   structural design is unique.  Through evolution-   rate of growth with the latter responsible for 

                   ary development organisms develop struc-           the shape or curvature of its surface.  From this 

                   tural enhancements that prevent environmen-        it is possible to derive a relationship between 

                   tal damage to themselves rather than having        the form of the object and the space it occu-

                   the ability to repair themselves once damage       pies.  The external environment exerts a pres-

                   has occurred.                                      sure on the developing object and its resulting 

                   Mollusks are strong and tough composites that      form is a product of its response to the envi-

                   have the ability to prevent structural failure     ronment and the limits of the structural prop-

                   due to their unique microstructure.  Ceramic       erties of the material used.  It is a culmination 

                   layers imbedded in a proteinaceous matrix are      of interacting internal and external forces.  An 

                   oriented at different angles to redirect crack     organism in nature grows along the lines of 

                   propagation.  (Srinivasan 1996, p19).  See Fig-    greatest stress and it is this act of balancing the 

                   ures 38 & 39.                                      forces of stress and strain that give an object 

                                                                      its inherent structural characteristics.

                                                                   27

## [p. 50]

_(página sin capa de texto)_

## [p. 51]

3.0    Biomimetic Principles of  

                      Form in Architecture

                    Architecture has long been inspired by and infused with 

                    natural forms, where a building may reference a particular 

                    organic form yet may exhibit none of the physical advantages 

                    that it could lend to an innovation or extension of archi-

                    tectural technology.  Alternatively, a building may not allude 

                    to an individual organic form yet its function with regard to 

                    structure, mechanical or circulatory systems may be a direct 

                    result of investigations into natural principles of design and 

                    construction.  This thesis concentrates on the latter, where 

                    the architecture develops from or utilizes the biological sci-

                    ence that it derives inspiration from.  The examples of built 

                    form outlined in the following section are presented here 

                    not because they are said to represent instances of organic 

                    or zoomorphic architecture, but because they are suitable 

                    examples of curvilinear forms whose defi nition is rooted 

                    in the natural geometric or organizational rules that defi ne 

                    them. 

                                29

## [p. 52]

3.1 Built Examples:

                                                                     Antoni Gaudi – Sagrada Familia – “Everything 

                                                                     comes from the great book of nature.”  (Cra-

                                                                                      th

                                                                     ven 2006)  This 19  century architect closely 

                                                                     observed natural forms and was a bold inno-

                                                                     vator of advanced structural systems.  He 

                                                                     designed ‘equilibrated’ structures (that stand 

                                                                     like a tree, needing no internal bracing or 

                                                                     external buttressing) with catenary, hyperbolic, 

                                                                     and parabolic arches and vaults, and inclined 

                                                                     columns and helicoidal (spiral cone) piers, fi rst 

                                                                     cleverly predicting complex structural forces 

                                                                     via string models hung with weights (his results 

                                                                     now confi rmed by computer analysis).  (Pear-

                                                                     son 2001, p11)  See Figure 40. 

                                                                     “The most important requirement for an 

                                                                     object that is to be considered beautiful is that 

                                                                     it fulfi ll the purpose for which it is destined, 

                                                                     not as if it were a matter of gathering together 

                                                                     problems solved individually and assembling 

                                                                     them to produce a heterogeneous result, but 

                                                                     rather with a tendency toward a unifi ed solu-

                                                                     tion where the material conditions, function, 

                                                                     and character of the object are taken care of 

                                                                     and synthesized, and once the good solutions 

                                                                     are known it is a matter of taking that one 

                                                                     which is most fi tting to the object as deduced 

                         40.  Sagrada Familia.                       from the need to attend to its function, char-

                                                                     acter, and physical conditions.” (Martinelli 1967, 

                                                                     p125)

                                                                     Gaudi was an architect who believed that if 

                                                                     one looks for functionality in a design then he 

                                                                     will ultimately arrive at beauty.  He thought 

                                                                     that if it is beauty that is sought then it is only 

                                                                  30

## [p. 53]

art theory, aesthetics, or philosophy that will 

                    be reached.  Gaudi was able to recognize the 

                    endless variety of structural forms in nature and 

                    deduced that there is great wisdom in studying 

                    natural structures that are subjected to grav-

                    ity, look for fi nal solutions, and have evolved 

                    maximum function over millions of years.  He 

                    sought to gain a knowledge of these structures 

                    and bring them into the architectural realm.  

                    Gaudi’s design principles coalesced into a new 

                    theory that united three previously disparate 

                    areas of architecture where:  “...the mechani-

                    cal fact is geometrically demonstrated and is 

                    translated into three-dimensional material, 

                    making it structural.  Mechanics, geometry and 

                    structure have been synthesized to produce a 

                    logical architecture in which each active ele-

                    ment fulfi lls its function in an equilibrated way 

                    and with the least effort.” (Martinelli p134)

                    “The helicoid is the form of a tree trunk, and 

                    Gaudi used this form in the columns of the 

                    Teresian School.  The hyperboloid is the form 

                    of the femur, a form he used in the columns 

                    of the Sagrada Familia.  The conoid is a form 

                    frequently found in the leaves of trees, and this 

                    form he used in the roofs of the Provisional 

                    Schools of the Sagrada Familia.  The hyperbolic 

                    paraboloid is formed by the tendons between 

                    the fi ngers of the hand, and he built with this     41.  Palazzetto dello Sport. 

                    form the porch domes of the church crypt in 

                    the Guell Estate.” (Nonell 2000)

                    Pier Luigi Nervi – Palazetto dello Sport, Han-

                    gar – Italian architect/engineer responsible for 

                    a series of constructions based on the form of 

                    the equiangular spiral that appears with regu-

                                                                     31

## [p. 54]

stress and static equilibrium with greater free-

                                                                                                   dom from convention than was ever before 

                                                                                                   possible.  In order to reduce the cost of con-

                                                                                                   struction the material could be easily prefabri-

                                                                                                   cated in plaster molds.  This approach allowed 

                                                                                                   the building - skin and structure - to become 

                                                                                                   one cohesive unit.  (Leslie 2003, p45).  See Fig-

                                                                                                   ure 41.

                                                                                                   Eugene Tsui – Tsui has designed and built a 

                                                                                                   number of projects that have developed 

                                                                                                   through his fascination with nature and the 

                                                                                                   process of evolutionary biology that he is heav-

                                                                                                   ily involved.  His works take their inspiration 

                                                                                                   from a variety of organisms whose different 

                                   42.  Tsui’s Ecological House of the Future.                     structural and functional characteristics inform 

                                                                                                   the individual projects to which they are asso-

                                   larity in the natural world.  Nervi looked to                   ciated.  While his projects are expressly zoo-

                                   nature as a teacher that seeks to achieve opti-                 morphic in character they are always infused 

                                   mal results with minimal effort, while also cre-                with natural design principles that underlie the 

                                   ating harmony where beautiful proportions                       forms.  Tsui has performed extensive structural 

                                   and relationships manifest themselves through                   testing on a number of natural forms and uses 

                                   mathematic principles.  He experimented with                    his results to develop his architecture.

                                   these principles to establish a harmonious rela-

                                   tionship between the internal reinforcement                     “Dr. Tsui is not imitating nature’s shapes. He 

                                   and the external skin that enveloped it (Por-                   is attempting to enter into the very “mind” of 

                                   toghesi 2006).  The ability to develop these del-               nature—the source which creates the forms 

                                   icate forms came when Nervi made a break-                       and processes—and apply this knowledge to 

                                   through in the fi eld of reinforced concrete: the               create a new architecture, a new attitude of 

                                   invention of ferro-cemento.  This material was                  our living environments. No other architect in 

                                   formed using steel mesh as a core with layers                   history has looked deeply into nature, in a rig-

                                   of cement mortar brushed on top of it. The                      orous and scientifi c way, and then apply these 

                                   steel mesh was thin, fl exible, and elastic, and                discoveries to architecture.” (Tsui 2006).  See 

                                   its addition to cement created material which                   Figure 42.

                                   could withstand great strains. Ferro-cemento 

                                   enabled Nervi to design any form he wanted, 

                                   giving him a way to address the problems of 

                                                                                               32

## [p. 55]

3.2 Unbuilt Examples:

         Ken Yeang – Bioclimatic Architecture  – 

         Yeang’s designs follow the theme of ‘urban 

         ecosystem’, a holistic design solution that deals 

         actively with milieu for pedestrian fl ows, plant 

         growth and the equilibrium of energy, waste 

         and water.  Yeang believes that all architecture 

         ought to respond ecologically to the natural 

         environment as a whole.  His designs aspire 

         to making a direct contribution to a sustain-

         able ecological future.  (Yeang 2002) See Fig-

         ure 43.

         Peter Testa – Carbon Tower – Helical struc-

         tural system that puts a heavy reliance on ten-

         sile forces and the use of redundancy in mate-

         rial to prevent complete failure of the system 

         if a localized failure occurs.  All of the build-

         ing components are constructed of the same 

         material that is woven together and eliminates 

         the structural ineffi ciency of joints.  (Knecht 

         2006)  See Figure 44.

         EMERGENT Architecture – Radiant Hydronic 

         House - A prototype house that was devel-

         oped through a feedback of various building 

         systems into one another in an effort to pro-

         duce emergent effects, both quantitative and 

         qualitative.  The structure of the house is com-

         posed of a set of fl exible bands which function 

         at different levels of behavior from structural 

         to mechanical to circulatory based on both 

         the local environmental requirements as well 

         as on the behavior of the adjacent members.

                                 43.  Yeang’s bioclimatic skyscraper.  

                                33

## [p. 56]

A central spine satisfi es the environmental 

                                                                                                    requirements by unifying them into a mono-

                                                                                                    coque structure.  The ductwork also functions 

                                                                                                    as structural support and circulation platform.  

                                                                                                    The building systems of the house were con-

                                                                                                    ceived of not as singular entities that were 

                                                                                                    individually optimized rather the design sought 

                                                                                                    to optimize the function of the whole.  (Emer-

                                                                                                    gent 2005a)  See Figure 45.

                                                                                                    EMERGENT Architecture – Lattice House - 

                                                                                                    A design proposal for Vitra based on a mono-

                                                                                                    coque structure that strives to integrate every 

                                                                                                    level of building system from structural to elec-

                                                                                                    trical into one three-dimensional latticework 

                                                                                                    that is generated by its spatial morphology.  

                                                                                                    The Lattice House is a fl exible array of space 

                                                                                                    that contains in its genesis a diverse amount of 

                                                                                                    morphological possibilities for its fi nal form.

                                                                                                    The project uses Inverse Kinematics ‘bones’ in 

                                                                                                    order to generate a multidirectional array that 

                                                                                                    maintains a dynamic coherence in the system. 

                                                                                                    The framework functions simultaneously as 

                                                                                                    primary structure and mechanical infrastruc-

                                                                                                    ture.  A whole structure heat-exchange sys-

                                                                                                    tem, essentially a 3D radiator, capable of heat-

                                                                                                    ing and cooling the space is created without 

                                                                                                    the use of forced air by fi lling the structural 

                                                                                                    struts with water.  Struts also evolve locally 

                                                                                                    into stairs, bridges, and secondary propping 

                                                                                                    elements.

                                                                                                     The fi nal design was derived through ‘breed-

                                                                                                    ing’ the structurally fi t iterations of the design 

                                                                                                    that were subjected to structural loading anal-

                                   44.  Testa’s carbon tower.                                       ysis.  (Emergent 2005b)  See Figure 46.

                                                                                                34

## [p. 57]

3.3     Use of Structural Form in Archi-

                           tecture:

                   The architects and projects listed here are 

                   representative of a larger collection that 

                   have sought or are seeking to derive innova-

                   tive structural solutions through an effi cient 

                   use and understanding of geometry and its 

                   relevance in construction.  The research and 

                   development techniques utilized span the 

                   spectrum from physical modeling to intensive 

                   digital development and analysis.  While all of 

                   these designers may not pursue an explicitly 

                   biomimetic approach in their designs it is evi- 45.  EMERGENT Architecture’s radiant hydronic house.

                   dent that many of their designs contain under-

                   lying geometry or principles that are found in 

                   nature.  The implication here is that with a bet-

                   ter understanding of nature’s design and con-

                   struction principles it becomes easier to pro-

                   duce complex forms that contain an elegant 

                   simplicity.  

                   Designers with projects that invoke design lan-

                   guages that rely on complex geometries.

                       Antoni Gaudi

                       Victor Horta

                       Frei Otto

                       Felix Candela

                                                                   46.  EMERGENT Architecture’s lattice house.

                   Current designers utilizing complexly curved and 

                   nonlinear members and surfaces

                       Morphosis

                       Santiago Calatrava

                       Norman Foster

                       Coop Himme(l)blau

                                                                35

## [p. 58]

NOX – Machining Architecture

                                                                                                Pompidou Two - In an effort to reduce struc-

                                                                                                tural hierarchy and complexity of the exte-

                                                                                                rior surface the project was conceived of as 

                                                                                                using geometries that transition from single 

                                                                                                curvature to double curvature.  Long, linear 

                                                                                                elements acting as primary members where 

                                                                                                derived with straight rules or simple arcs.  A 

                                                                                                bifurcating lattice branched from the primary 

                                                                                                elements to produce a doubly-curved lattice 

                                                                                                that much like the shell of an arthropod does 

                                                                                                not rely on a hierarchy of primary and second-

                                                                                                ary structure.  See Figure 47.

                                  47.  NOX:  A-life, an earlier version of Son-O-house.         Surface to line – Effectively covering a dou-

                                                                                                bly-curved surface continues to be a challenge 

                                                                                                for designers.  In Parc Guell, Gaudi had the 

                                                                                                idea of using waste pieces from regular square 

                                                                                                tiles that had broken on the factory fl oor.  The 

                                                                                                polygonal elements created a pattern of cracks 

                                                                                                on the benches that occurs in craquelure and 

                                                                                                Voronoi diagrams.  Spuybroek’s thoughts on 

                                                                                                surfacing then shifted from thinking in joints to 

                                                                                                thinking in cracks.  His idea was to segment the 

                                                                                                surface during geometrical formation instead 

                                                                                                of beforehand.  The desire is to develop the 

                                                                                                geometric form, structural form and panel-

                                                                                                ization in a concurrent manner rather than 

                                                                                                sequentially.  This type of process leads to the 

                                                                                                feedback scenarios associated with natural 

                                                                                                constructions.  

                                  48.  NOX:  Structural ribs defi ning a doubly-curved          Line to surface – Typical surfacing procedures 

                                  surface are clad in narrow woods strips the follow the 

                                  curvature much like in shipbuilding.                          consist of breaking the developed surface into 

                                                                                                lines.  Spuybroek outlines a fascination with a 

                                                                                                Gothic type of logic where lines bifurcate and 

                                                                                            36

## [p. 59]

weave themselves into surfaces.  The simple 

                    curves begin to develop patterns of interlac-

                    ing that evolve into larger and more complex 

                    confi gurations that satisfy not only aesthetic 

                    but structural requirements.  The Gothic build-

                    ers were able to develop and use arabesque 

                    patterns that transcended a strict ornamental-

                    ity.  (Spuybroek 2004e)

                    Son-O-House - Once again the issue of panel-

                    ization of doubly-curved surfaces arises where 

                    Spuybroek regards tessellation as the sub-

                    division into or addition of tile modules to a 

                    surface.  The least interesting yet often most 

                    cost effective method of tessellation is trian-

                    gulation, where the surface is partitioned into 

                    triangular facets each of which is planar.  A 

                    variable approach based on textiles was used 

                    here where fl exible bands are able to create 

                    a substrate for the hardened tile.  (Spuybroek 

                    2004g)

                    ECB - In this design for the European Central 

                    Bank, Spuybroek looked to Radiolaria (micro-

                    organisms around 0.1 mm in size) for inspira-

                    tion.  See Figure 49.  “The amazingly beauti-

                    ful drawings of Ernst Haeckel from the early 

                    1900s and the research of Helmcke and Otto 

                    throughout the second half of the twentieth 

                    century show that Radiolaria are of a highly         49.  NOX:  Design for the European Central Bank 

                    architectural nature.  See Figure 50.  For these     based on Radiolaria morphology.

                    German bioconstructivists this is another 

                    argument in favor of the idea that a substan-        and second, that isomorphism is not fatally 

                    tial part of the living form is non-genetic in       attracted to the Sphere but is the generator 

                    origin.  What makes the study of Radiolaria so       of ribs, spikes, creases, tubes, and the like.  Vari-

                    relevant is that it teaches us that variation is a   ation within the system can produce variation 

                    product of uniformity or, better, isomorphism;       of the system.” (Spuybroek 2004b)

                                                                      37

## [p. 60]

50.  Ernst Haeckel’s drawing of Radiolaria from the 

                                     Family Spongurida.

                                    38

## [p. 61]

4.0    Investigation Into Surfaces  

                              and Manufacturing

                     While it is possible to derive effi cient structural forms from 

                     a biomimetic investigation into natural designs, their logi-

                     cal development and effi cient translation in built form must 

                     occur with knowledge of the geometric principles inherent 

                     in them.  A mathematical analysis of surface and curve defi -

                     nition serves to allow for a reliable and informed transla-

                     tion from physical observation into digital generation.  The 

                     methods for physical construction of a design are outlined 

                     in an attempt to align the biomimetic investigations with the 

                     realities of current construction technologies.  While some 

                     natural design and construction methods may be highly effi -

                     cient and ideal for architecture, their realization as manmade 

                     constructions may not be possible until current technologies 

                     evolve further or new ones are developed.  

                                 39

## [p. 62]

4.1    Curved Surfaces – Defi nition,                 most closely traces and passes through the 

                                       Generation and Analysis                      curve at that point and has a center point tan-

                                                                                    gent to that point.  The curvature is essentially 

                              Perhaps the most obvious way in which design-         the reciprocal of this instantaneous value.  The 

                              ers have benefi ted from the advancement of           smaller the radius of the curve is, the larger the 

                              digital design software is in the realm of curved     associated curvature will be and vice versa.

                              and complex surfaces.  However, there are 

                              trade-offs that frequently arise with various         The parabola is composed of a constantly 

                              programs and their effective utilization at cer-      changing curvature gradient whose instanta-

                              tain points in the design and construction pro-       neous radius at its apex will be quite smaller 

                              cess.  The starting point for many architects is      than that at its end.  This characteristic of a 

                              to create a surface model that closely approxi-       varying curvature from point to point can be 

                              mates the shape and form that is desired.  This       seen in most other curves between the straight 

                              process can occur rapidly and changes are also        line and circle.  Like the values for the instanta-

                              readily accomplished.  Once the surface model         neous radius which exist at an individual point, 

                                                                                    so too does the instantaneous curvature rely 

                              has been obtained it is then necessary to cre-        on individual points.  By selecting a point (A) 

                              ate a solid model that is derived from those          on a surface it is possible to derive a line that 

                              surfaces.  A solid model is essentially a volu-       is normal to the surface at the point (A).  It is 

                              metric representation where complex surfaces          now possible to obtain a surface plane which 

                              that defi ne the morphology of the model are          passes through point (A) and its normal line.  

                              numerically exact for proper manufacturing            This normal plane if extended to intersect the 

                              and construction.  Often times a program that         surface will create an intersection curve called 

                              excels at surface modeling is hindered when           the normal section.  Additionally, the instanta-

                              performing solid modeling and vice versa.  The        neous curvature at point (A) is referred to as 

                              development of solid models from surfaces             the normal section curvature.

                              can be accomplished through a number of               From Figure 51 it can be seen that the normal 

                              techniques which can have resounding effects          plane can be rotated in any increment around 

                              when it comes to manufacturing and construc-          the normal line which would lead to an infi -

                              tion.  (Schodek, 2005, p6)                            nite number of normal sections each with its 

                                                                                    own unique normal section curvature.  From 

                              4.1.1 Surface Curvature                               this it can be stated that throughout the num-

                                                                                    ber of normal sections there will be one max-

                              A curve can be mathematically described               imum value (k      ) and one minimum value 

                                                                                                    max

                              whereby at any point the shape of the curve           (k  ).  These two principal curvature values can 

                                                                                      min

                              will have an instantaneous radius (R) and an          be found by rotating the normal section plane 

                              associated curvature (1/R).  The instantaneous        until these values are found.   (Schodek 2005, 

                              radii can be thought of as defi ning a circle that    p195)

                                                                                40

## [p. 63]

4.1.2    Gaussian and Mean Curvature                  which in effect creates a straight line.  (Sch-

                                                                          odek 2005, p196)

                    Gaussian curvature can be thought of as being 

                    the product of the two principal normal section       4.1.3    Curvature Investigation and         

                    curvatures at a point where k  = k     x k  .  The         Representation

                                                   g   max    min

                    mean curvature k  is the average of k        and 

                                       m                      max

                    k .  A surface with a  positive Gaussian cur-         Many advanced modeling programs today 

                      min

                    vature can be referred to as synclastic where         have provision for analyzing surface curva-

                    the normal section curves have the same sign          ture.  These curvature values can be displayed 

                    in all directions.  These surfaces belong to all      numerically or visually depending on prefer-

                    concave and convex shapes and are nonde-              ence.  Colors or hues can be set to correspond 

                    velopable whereby the surface cannot be fl at-        to varying degrees of curvature as well as pos-

                    tened without material distortion.  A negative        itive and negative values.  With this technique 

                    Gaussian curvature in a surface is called anti-       the designer can quickly visualize the surface 

                    clastic where the principal curvatures are of         to determine whether it meets the desired 

                    opposite signs.  These surfaces are not devel-        shape and is free from unwanted deformities.  

                    opable either even though some are classifi ed        A complex surface form composed of a num-

                    as ruled surfaces.  If the Gaussian curvature is      ber of different surface curvatures can be also 

                    equal to zero everywhere on the surface then          be quantifi ed with regard to the degree and 

                    it can be fully developed into a fl at plane with-    type of curvature with respect to cost impli-

                    out any material distortion.  In this case one        cations.  On a monetary scale the expense of 

                    of the principal curvatures must equal zero           cladding panels will increase from planar to 

                    51.  Curvature of surfaces:  normal curvature and related principal values of a 

                    synclastic surface.

                                                                      41

## [p. 64]

doubly curved.  By visually defi ning the surface 

                                                                                   condition for the panels it is possible to get a 

                                                                                   graphical representation as to the proportion 

                                                                                   or areas of the façade that may be too expen-

                                                                                   sive and therefore require adjustment.  (Sch-

                                                                                   odek 2005, p196)  See Figure 52.

                                                                                   4.1.4    Conical sections and surfaces    

                                                                                            derived from them

                                                                                   Many complex surfaces if created with some 

                                                                                   comprehension of basic curves can be created 

                                                                                   by combining a number of these curves.  Coni-

                                                                                   cal sections for example are readily used to 

                                                                                   create curved surfaces that can be easily cal-

                                                                                   culated mathematically.  Through a number of 

                                                                                   different operations such as revolving, lofting, 

                                                                                   sweeping or any combination of the same it 

                                                                                   is possible to create domes, parabolic surfaces, 

                                                                                   barrel vaults, and hyperbolic paraboloids.  Of 

                                                                                   note here is the fact that these surfaces can be 

                                                                                   understood relatively intuitively and have the 

                                                                                   benefi t of being more easily created and man-

                                                                                   ufactured with less digital computation than 

                                                                                   more complex surfaces.

                                                                                   4.1.5    Ruled and Developable Surfaces

                                                                                   A ruled surface is any surface that can be 

                                                                                   derived from a translational sweeping, with 

                                                                                   optional rotation, of straight lines.  See Figure 

                             52.  Curvature analysis diagram.                      53.  The surfaces derived from these manipula-

                                                                                   tions can take the form of cylinders, cones, and 

                                                                                   conoids in one group, and hyperbolic parabo-

                                                                                   loids and hyperboloids in another.  However, 

                                                                                   while all of these shapes are deemed as ruled 

                                                                                   surfaces, there are two signifi cant differences 

                                                                               42

## [p. 65]

that separate these two groups where the fi rst 

         group consists of developable surfaces and the 

         second group nondevelopable.  Developable 

         surfaces have the ability to be unrolled or fl at-

         tened into a sheet without deformation.  Non-

         developable surfaces must be cut or deformed 

         in order to be constructed from a fl at sheet 

         of material.  

         4.1.6 Complex Surfaces

         The designs seen today in architecture quite 

         often take the form of surfaces whose defi ning 

         layout curves are becoming increasingly more 

         complex and not as easily defi ned as those 

         of the ruled and developable surfaces.  While 

         the creation of models with curves such as B-

         splines and NURBS can be carried out with 

         similar modeling techniques as to those men-

         tioned above, their mathematical derivation 

         and visual comprehension can far exceed 

         many simpler surfaces.  Added manufacturing 

         complexity also arises in these cases due to 

         the inherent inability of a planar surface to be 

         formed into a complex surface without either 

         extensive material working and deformation 

         or a much more elaborate method of faceting 

         to arrive at the desired confi guration.

                                 53.  Ruled surfaces

                                43

## [p. 66]

4.2      Primary Structural and Con-                 be easily erected out of fl at wood planks.  

                                      struction Specifi c Considerations          (Schodek 2005, p49)

                             4.2.1 Construction Considerations                    4.2.2 Structural Considerations 

                             Historically speaking, when geometrically  Structural effi ciency is an aspect of design that 

                             complex building forms were built, as with           may or may not be explicitly considered when 

                             the works of Victor Horta for example, they          generating complex building forms.  While 

                             respected the limitations of the current con-        many civil engineering structures that utilize 

                             struction technology.  The designer recognized       complex geometries (dams) are responsive 

                             their responsibility for expressing their design     to both structural and technical effi ciency, this 

                             intent through precise and comprehensible            is often not the case with regard to architec-

                             representations that could be understood by          tural constructions.  The simple act of form-

                             all of the parties involved in the project.  Even    ing a curved surface does not automatically 

                             designers seeking to create apparently non-          infuse it with the positive structural benefi ts 

                             defi nable forms began to develop new ways in        that are possible with certain curved surfaces.  

                             which to manufacture the complex geomet-             The classic doubly curved shapes such as por-

                             rical forms in line with the appropriate con-        tions of spheres or the hyperbolic paraboloid 

                                                                                  shapes used by architects in the late 19th

                             struction techniques.                                                                            and 

                                                                                          th

                                                                                  early 20  century have been widely proven to 

                             Between the period of 1914 to 1926 when              demonstrate “membrane action” where inter-

                             Antoni Gaudi worked on the Sagrada Familia,          nal forces are effi ciently transmitted through 

                             he developed a set of construction rules that        the surface of the shell in an in-plane manner.  

                             the masons were able to follow.  His genera-         See Figure 54.  When this scenario exists, the 

                             tion of the principal architectural elements was     stresses acting out of plane within the surface 

                             based on “ruled surfaces” which included the         are quite low and thus the shell can be made 

                             hyperbolic paraboloid and the hyperboloid of         quite thin.  Membrane action does not exist in 

                             revolution, both of which are doubly curved          all curved surfaces and its presence in a sur-

                             and non-developable.                                 face depends on the existence of particular 

                                                                                  combinations of surface shapes and types of 

                             While different in their architectural expres-       loading conditions.  It is important to note that 

                             sion, the later works of Felix Candela and           with a corresponding decrease in the amount 

                             Pier Luigi Nervi used the same conceptual            of material associated with the proper devel-

                             approach as Gaudi.  These men made exten-            opment of a structural skin that exhibits mem-

                             sive use of those kind of surfaces in the rein-      brane action the skin will also be more sus-

                             forced concrete structures that they designed.       ceptible to deformation due to local or point 

                             In this manner the wooden formwork could             loads.  A proper balance between these must 

                                                                              44

## [p. 67]

be met or the design of the membrane must 

                   act on a variety of levels to redistribute stresses 

                   imposed on it.

                   The misconception that curvature automati-

                   cally translates into structural effi ciency is quite 

                   prevalent in construction today.   Complexly 

                   curved surfaces and their widespread use 

                   can often be immature versions of properly 

                   designed surfaces that could potentially exhibit 

                   the desired characteristics of membrane action.  

                   It is only through careful examination of the 

                   design, functional criteria and intent along with 

                   structural analysis can the fi nal product exhibit 

                   the structural advantages associated with a 

                   curved surface.  (Schodek 2005, p48)

                                                                      54.  Roof of Nervi’s Palazzetto dello Sport which 

                   4.3      Defi ning Surface Shapes                  exhibits membrane action

                                                                      Uncommon – The designers develop compu-

                   4.3.1 Digital Form-Generation Techniques   tational environments whereby the design is 

                            and Shape Generation                      developed by the program through pre-speci-

                                                                      fi ed rule structures or other principles.

                   Many of today’s computationally based design 

                   approaches to complex geometric forms  The most widely used approach for shape 

                   focus on arbitrary form generation, with mini-     generation used by designers is the direct 

                   mal attention paid to manufacturing, construc-     use and manipulation of computational tools 

                   tion and structural effi ciency.                   (points, lines, splines, lofts, sweeps, etc.) com-

                                                                      monly found in a variety of digital modeling 

                   Common vs. Uncommon Approaches                     environments (form-Z, Rhinoceros, MicroSta-

                                                                      tion, etc.).  

                   Common – The designs are envisioned by 

                   the user and the digital tools act to develop      Computational tools that are visually ori-

                   and represent these ideas.  The inspiration for    ented and based on descriptive geometry or 

                   complex and unique shapes is derived from          on other mathematical means of describing 

                   many different sources, ranging from direct        lines, curves, and surfaces can also be used in a 

                   responses to programmatic requirements.            more direct manipulation process to generate 

                                                                      forms.  Software technologies associated with 

                                                                   45

## [p. 68]

this type of shape derivation are uncommon        A recent trend is based on an approach that 

                            in the architectural design environment but       seeks to derive form through the implemen-

                            are found in broad based mathematical tools       tation of genetic growth or repetition algo-

                            (MathCAD, Mathematica, Maple).                    rithms.  Patterns seen in nature such as frac-

                                                                              tals and tessellations can be broken down into 

                            In an effort to derive forms based on a set of    complex rule structures that can be in turn 

                            external infl uences be they real or metaphori-   modifi ed and used for shape generation.

                            cal, some designers have adopted the use of 

                            software (Maya) that allows for an infl uence of  The idea of time and temporality in architec-

                            form based on force functions of on type or       ture is often overlooked and it is in this regard 

                            another.  Objects or functions within an envi-    that some architects (Kas Oosterhuis and Ole 

                            ronment can be given a defi ned set of control-   Bauman) have sought to develop buildings that 

                            lable parameters that afford them the ability to  effectively change throughout time and to var-

                            infl uence and interact with other objects that   ious external forces.  Here, architects are not 

                            can in turn push, pull, deform and essentially    designing static structures that maintain their 

                            drive shape generation for the resultant form.    structural form but ones that are capable of 

                                                                              adapting to new uses or needs.  Just as cul-

                            Parametrically driven shape derivation is also    tural changes occur over time, these buildings 

                            being used in a more controlled manner,           would modify their layout and organization to 

                            whereby the forms are generated accord-           best serve the immediate needs of the user 

                            ing to sets of predefi ned rule structures and    with the possibility to serve future uses equally 

                            component parts.  The design approach within      well.  Digital environments that support ani-

                            these software applications can vary from         mation and motion (Maya) are useful here.

                            one to another where priority can be placed 

                            on having a strong construction rationale or      4.3.2    Physical Model to Digital Model

                            through different programmatic or concep-

                            tual intents (Generative Components, CATIA, 

                            SolidWorks, Unigraphics, CADDS5).  A com-         While the digital environment can be invalu-

                            monly used approach here is to defi ne a set      able when deriving, representing and promot-

                            of parameters for a structural element whose      ing designs to construction, a great number of 

                            form drives the formation of the building enve-   architects still rely on physical modeling tech-

                            lope.  The parameters defi ned can be related     niques as a rapid and tactile way in which to 

                            to the physical dimensioning of a component       arrive upon a desired formal scenario.  The 

                            or any number of relevant values or relation-     models of churches, cathedrals and other 

                            ships.  Through direct manipulation of these      buildings that remain from centuries ago are 

                            control parameters the changes will propa-        incredible reminders of how valuable physical 

                            gate throughout the model to instantaneously      modeling can be both in design and prelimi-

                            update it.                                        nary structural analysis.  Digital scanning tech-

                                                                           46

## [p. 69]

niques and computationally based program-           be confused with the computational systems 

                    ming software now allow architects to scan          described here which include the force-density 

                    a physical model for promotion into a digital       method and the dynamic relaxation technique.  

                    model which in turn allows for the production       Both of these are designed to minimize the 

                    of a physical model for further physical manip-     embodied potential energy and balance the 

                    ulation.  Once the physical model has reached       forces in the system through the optimization 

                    its desired confi guration then the project can     of the building form itself.  The optimal shape 

                    progress for subsequent development in the          is one that maintains equilibrium between the 

                    translated digital form.  The process of digi-      external loads applied to it and the internal 

                    tal scanning is still relatively raw in practice    forces that resist these loads with a subse-

                    because the scanner will create a set of sur-       quent minimization of material.  Whether it be 

                    faces derived from the physical model that          through physical or digital form fi nding tech-

                    the program must then be manually guided to         niques, the manipulation of form is only possi-

                    stitch together.  This surface model must then      ble through changes in loading of the structure 

                    be translated into a solid model through the        or to the support and boundary conditions 

                    appropriate program.  (Schodek 2005, p52)           with each resulting in a unique shape.

                    4.3.3    Form Finding Through Structural            4.3.4    Structure and Enclosure

                         Viability

                                                                        When designing a surface enclosure that is 

                    The digital techniques of form generation           composed of compound curves there are 

                    illustrated up to this point are all methods in     many considerations that need to be addressed 

                    which to conceptualize and generate complex         early within its development.  Included in these 

                    surfaces.  The forms derived from these how-        is the question of whether the surface will be 

                    ever, do not necessarily translate into viable      required to be structural or not.  If the surface 

                    structural systems with effi cient methods for      is intended to be structural then there must be 

                    production and construction.                        the associated investigations into whether the 

                                                                        surface is also load bearing with regard to live 

                    Previous to digital computation software it         and dead loads as well as natural forces such 

                    was through accurate physical models (hang-         as wind and earthquake.  If the surface is not 

                    ing chains, minimal surface experiments with        intended to be structural then its relation to a 

                    soap or stretch fabric) that structural form        primary structure must be developed.  In line 

                    fi nding was carried out.  These approaches         with structural considerations are the require-

                    are still effective today with the possibility for  ments for glazing/transparency, energy require-

                    their promotion into the digital environment        ments, material viability, ease of construction, 

                    through 3D scanning techniques.  The compu-         maintenance and other factors involved in the 

                    tational approaches outlined above should not       design of any enclosure.

                                                                     47

## [p. 70]

Another question is whether the exterior sur-       Slab support system – On a larger structural 

                             face relates to the interior surface whereby        scale and in a project with multiple fl oors it is 

                             there is a single defi ning surface.  If so then    the fl oor plates themselves that can become 

                             both the enclosure and structure must be            the horizontal sectional planes with the exte-

                             combined into one system.  If the exterior and      rior panels spanning between them.  See Fig-

                             interior spaces are unrelated then the struc-       ure 55.

                             tural system has the possibility to occupy the 

                             interstitial spaces between them which invari-      The creation of a smooth doubly curved sur-

                             ably allows for a greater degree of design          face will usually require the integration of sur-

                             choices.                                            face and structure together as in a structural 

                                                                                 shell or where the structural elements and 

                             4.3.5    Approaches to Building a Large             the surface enclosure are curved.  When the 

                                      Compound Curved Surface                    structural scale with regard to the surface size 

                                                                                 is increased then the surface will have a ten-

                             Subdivide the surface – Lines of structural         dency to become more faceted and conform 

                             framing are placed to correspond with the           less to the desired shape.  This has the prac-

                             surface division.  Smaller, lightweight enclosure   tical implication of reducing build complexity 

                             panels then span between the primary struc-         and cost.  (Schodek 2005, p54) 

                             tural elements.  In this scenario the primary 

                             structural elements would often be composed         4.4      Structural Surfaces – Translation 

                             of compound curves and the associated enclo-                 from Digital Design to Physical 

                             sure panels would be doubly curved.  In an                   Fabrication

                             effort to reduce the complexity of this system 

                             it is possible to compose the structure of pla-     When designing a building in a relatively unre-

                             nar facets that are connected to linear struc-      strictive digital environment it is often useful 

                             tural members.  (Schodek 2005, p200)                to have an idea of the type of building material 

                                                                                 to be used and the construction techniques 

                             Sectional planes at regular intervals – By divid-   involved with the use of that material or sys-

                             ing the structure into a set of repeating sec-      tem.  With an idea of the possibilities and limi-

                             tional planes it is possible to design structural   tations inherent with use of a particular mate-

                             members that although curvilinear remain pla-       rial and construction approach the designer 

                             nar with the surface and as such avoid com-         can avoid spending time on creating forms 

                             pound curves.  An egg crate pattern begins to       that are unrealistic with regard to their devel-

                             develop when horizontal sections are passed         opment and manufacture.

                             through the structure as well which allows for 

                             smaller enclosure panel sizes.  See Figure 55.

                                                                              48

## [p. 71]

4.4.1 Large Continuous Surfaces

                   There is a wide range of material possibilities 

                   for manufacturing curved surfaces, from rein-

                   forced concrete all of the way to pre-stressed 

                   structural fabrics.  The techniques associated 

                   with their construction vary widely as well.  In 

                   the case of reinforced concrete and classic 

                   masonry construction there is often an intri-

                   cate system of formwork involved to achieve 

                   the fi nal form.  This approach has been aided 

                   with the use of CAD/CAM technology where 

                   the formwork can be CNC machined to pro-

                   vide the proper curvature.  It is the incredible 

                   surface fl uidity that is achievable with poured 

                   concrete that continues to attract architects 

                   today.

                   Where the structure itself is composed of 

                   intricately carved stone there has been a tra-

                   dition of manual carving which is labor inten-

                   sive and costly in today’s market.  While this 

                   approach has been updated with the use of 

                   CNC cutting, milling and routing machines as    55.  Strategies to support complexly shaped surfaces.

                   in the new work being done on the Sagrada 

                   Familia in Spain, it still remains an issue of cost 

                   for many.  In an effort to reduce material costs 

                   this scenario has been reduced to affi xing a 

                   thin stone veneer to a distinct structural core.

                   Wood has a history most notably in shipbuild-

                   ing for being shaped into curvilinear forms.  

                   The relatively recent technology of glue-lam-

                   inated lumber has added another dimension 

                   to the structural possibilities of wood in addi-

                   tion to the ability of CAD/CAM technology to 

                   both provide data for the construction of the 

                                                                49

## [p. 72]

required jigs as well as making viable the cre-        With the use of CAD directed fi nite-element 

                              ation of complexly curved surfaces.                    analysis of a proposed structure in its digital 

                                                                                     form, it is possible to develop strategies for built 

                              The panelized unit which is usually constructed        up and layered composite systems that derive 

                              of thin sheet metallic, polymeric or composite         their strength or additional strength from the 

                              materials has typically been diffi cult to develop     directional placement of individual strips along 

                              into a system that in itself works as a struc-         the lines of force contained within the surface.  

                              tural system.  It is often necessary to provide a      By applying material along the direction of 

                              secondary stiffening system.  In the same way,         the forces involved there is a reduction in the 

                              surfaces consisting of woven or layered strips         amount of material necessary to resist those 

                              cannot function effi ciently unless multiple           localized forces.  See Figure 56.

                              cross bonded layers are used to achieve the 

                              required cross-sectional structural depth.             Doubly curved metal panels have continued 

                                                                                     to remain of interest to architects that desire 

                              4.4.2    Small Continuous Surfaces                     a curved surface that can be structurally sup-

                                                                                     portive and weather resistant with the desired 

                              Advances in material forming have allowed the          fl uid and monolithic aesthetic.  Smaller units 

                              production of complex surfaces that exhibit            can be molded or stamped while larger pan-

                              structural capabilities and are well suited for        els which are inherently nondevelopable must 

                              relatively small structures.  As the forces begin      undergo extensive deformation or slicing with 

                              to multiply for larger structures, the structural      subsequent rejoining to achieve a compound 

                              possibilities associated with these materials          surface.  Numerous cold forming techniques 

                              begin to diminish and are usually inadequate           are available to the designer including rolling, 

                              to serve for these larger structures.                  stamping and planishing.  These techniques, 

                                                                                     with the exception of rolling, require a con-

                              Fiberglass has historically been used in a             siderable investment in either time or tooling 

                              wide variety of applications to create large,          which can become cost prohibitive if there are 

                              smooth, and stiff surfaces.  Within the auto-          a large number of unique pieces to be made.  

                              motive, aerospace and naval industries, the            (Schodek 2005, p55-58)

                              use of fi berglass has essentially involved laying 

                              multiple resin-impregnated strips or sheets of 

                              fi berglass over a curved framework for cur-

                              ing.  Advancements in the composites industry 

                              have produced materials (carbon fi ber, kevlar) 

                              that offer incredible structural properties with 

                              a drastic reduction in the amount of material 

                              necessary and as a result a reduction in the 

                              dead weight of the structure.  

                                                                                  50

## [p. 73]

4.4.3 Surface Enclosure

                  If the surface itself is not capable of handling 

                  the intrinsic structural forces that must be 

                  resisted then it is necessary to introduce a pri-

                  mary structural system that can.  The outer 

                  surface of the building then becomes predom-

                  inantly non-load bearing with the only struc-

                  tural requirement being that of resisting local 

                  loading.  This approach typically sees the pri-

                  mary structure designed according to a less 

                  complicated method of manufacture and con-

                  struction.  If the interior and exterior forms dif-

                  fer drastically it may be necessary to introduce 

                  a secondary structural system that is a means 

                  of connection between the primary structure     56.  Directional layers of fi berglass laminated to a 

                  and the façade.  The most complicated prob-     formed balsa core

                  lem with this technique is the derivation of the 

                  correct offsets and positioning of the second-

                  ary members and their corresponding attach-

                  ment points to both the primary structure and 

                  the surface as well.  This process is simplifi ed 

                  with the use of advanced CAD technology, 

                  however the suitable programs are quite dif-

                  fi cult to learn/use and may be cost prohibitive 

                  for many designers.  See Figure 57.

                  4.4.4   Thin Sheet Surfaces

                  On a small scale it is possible to manufacture 

                  complex surfaces through the use of CNC 

                  produced forms where the chosen surface 

                  material is subsequently formed or stamped 

                  directly on it.  Metal panels can be produced 

                  in this way but they are often limited to thin 

                  wall sizes and small bounding dimensions.  As 

                  the size and thickness of the metal sheets 

                                                              51

## [p. 74]

increase they become increasingly diffi cult to 

                                                                                                deform and produce the desired complex 

                                                                                                shapes.  Due to the limited thickness possi-

                                                                                                bilities for stamping the use of metal panels 

                                                                                                here is limited to a surface condition that pro-

                                                                                                hibits them from performing in a load-bearing 

                                                                                                capacity without deformation.  Curvature in 

                                                                                                one dimension however can be easily accom-

                                                                                                plished through rolling and as such allows for 

                                                                                                panels with greater size and thickness.  This 

                                                                                                enables the designer to reduce the secondary 

                                                                                                system required for attachment to the primary.  

                                                                                                Depending on the complexity of the skin con-

                                                                                                fi guration a balance must be met between the 

                                                                                                formability of the individual steel panel and the 

                                                                                                complexity of the secondary system.  

                                                                                                The evolution of a traditional method for steel 

                                                                                                fabrication is in development by the Navy 

                                                                                                Joining Center (NJC) along with a number of 

                                                                                                other partners.  The technique called Auto-

                                                                                                mated Thermal Plate Forming (ATPF) is a pro-

                                                                                                cess whereby numerical modeling, digital mea-

                                                                                                surement and intelligent computer feedback 

                                                                                                programs will work in concert to produce 

                                                                                                repeatable, high accuracy formed steel plates.  

                                                                                                This process of thermal formation is currently 

                                                                                                performed by skilled operators using oxy-fuel 

                                                                                                torches and manual quenching with water.  

                                                                                                While both approaches allow for the forma-

                                                                                                tion of simple and compound curvatures the 

                                                                                                manual approach is quite labor intensive and 

                                                                                                limited by the experience of the operator.  The 

                                                                                                automated system is composed of four mech-

                                                                                                anisms including path planning software (PPS), 

                                                                                                an induction heat source (laser), a manipulation 

                                  57.  Relationships between skin and structure for             and plate holding device, and an automated 

                                  complex surfaces.

                                                                                            52

## [p. 75]

measurement system (AMS).  The PPS will              where thin strips of material will bend into a 

                     produce a required set of heating paths and          defi ned shape when attached at the ends and 

                     parameter sets based on the desired 3D con-          specifi c points in between.  The bendability 

                     formation (CAD derived) and the initial plate        of thin strip materials often requires that the 

                     shape which incidentally is not limited to a pla-    surface be composed of broad fl owing forms 

                     nar confi guration.  The PPS will output data to     without abrupt surface deviations which coin-

                     the manipulation system that will direct both        cidentally prove appropriate for large surfaces 

                     the movement of the heating unit as well as          from ship hulls to facades of buildings.  Digital 

                     the plate itself.  Once the forming has occurred     models that utilize fi nite element analysis are 

                     the AMS will measure the fi nal plate shape and      useful here in that they can produce visual-

                     compare these values to the desired shape.  If       izations of primary stresses within the model 

                     necessary the PPS will automatically derive          which in turn can direct the placement of strips 

                     any new heating paths required to achieve the        in an optimal manner.  See Figure 59.

                     fi nal form.  This new technology has the ability 

                     to increase quality, decrease costs and reduc-       4.4.6    Aggregated Faceted Panels

                     tion production times.  The Navy expects that 

                     with regard to its DD(X) advanced multi-mis-         To avoid the associated diffi culties inherent in 

                     sion destroyer they will see a 100% increase         creating complex surfaces from non-develop-

                     in throughput, 80% reduction in rework, 50%          able fl at sheets, architects have resorted to 

                     reduction in direct labor costs, and 75% reduc-      dividing the surface into a number of smaller 

                     tion in support labor costs.  As can be imag-        units that consist of planar surfaces.  These 

                     ined the potential applications with regard to       facets may take the form of triangles or var-

                     architecture are widespread and the associ-          ious other shapes, but the key here is that 

                     ated cost reductions over conventional form-         their edge conditions are straight and as such 

                     ing methods will allow for its use on a greater      both manufacturing and constructability are 

                     number of projects.  (Coffey 2006)  See Fig-         made easier.  As the facets within the surface 

                     ure 58.                                              become smaller it is possible to produce a 

                                                                          smoother fi nished product but this can come 

                     4.4.5 Bendable Strips                                at the result of increased complexity, manufac-

                                                                          turing and material usage.  See Figure 60.

                     Long used in the shipbuilding industry, the appli-

                     cation of thin strips of material over a more        Digital modeling in this approach requires that 

                     complex rib system has proved quite success-         a grid be applied over the model and suitable 

                     ful in producing complex forms that exhibit a        panel sizes are derived from the resultant of the 

                     smooth and fl owing surface.  It is of interest to   intersection between grid and surface.  Projec-

                     note that spline curves so readily used in digi-     tion and mapping are two methods possible 

                     tal modeling today stem from the naval arena         for defi ning the surface grid.  Projection implies 

                                                                       53

## [p. 76]

simply that, a planar grid is projected directly 

                                                                                                onto the surface.  This produces panels that 

                                                                                                while looking identical in elevation are actu-

                                                                                                ally distorted in order to compensate for the 

                                                                                                surface curvature.  Mapping essentially wraps 

                                                                                                the surface with the predefi ned grid arrange-

                                                                                                ment.  This technique has the advantage of 

                                                                                                maintaining the desired panel shape for ease 

                                  58.  Thermal Plate Forming.                                   of manufacturing however it may be necessary 

                                                                                                to modify the surface shape to accommodate 

                                                                                                the limitations of the panels in producing the 

                                                                                                desired complex surface.  See Figure 61.

                                                                                                4.4.7      Shaped Primary Structural Elements

                                                                                                To maintain an architectural purity within a 

                                                                                                building that maintains a connection between 

                                                                                                inner and outer surfaces, it is desirable to pro-

                                                                                                duce a primary structural system that follows 

                                                                                                the shape of the exterior surface if not exactly 

                                                                                                then to a degree that minimizes the require-

                                                                                                ment of an elaborate secondary structural sys-

                                                                                                tem.  While it is relatively easy to accomplish 

                                                                                                these complexly shapes structural members in 

                                                                                                small scale applications such as in the automo-

                                                                                                tive and naval sector it becomes much more 

                                                                                                complicated in a large scale building where the 

                                                                                                structural elements can be quite massive and 

                                                                                                diffi cult to form.  Select rolling mills have the 

                                  59.  Fish Sculpture, Barcelona.  

                                                                                            54

## [p. 77]

capacity to bend large steel sections in one 

         direction but their capacity for out of plane 

         twisting is quite limited.  The bending machines 

         suitable for circular sections have the ability to 

         produce complex shapes although in practice 

         the sections lack the required strength and 

         stiffness to act as primary structural members.  

         (Schodek 2005, p59-61)  See Figure 62.

                                 60.  Swiss Re Headquarters, London. 

                                 61.  Surface subdivisions.  

                                55

## [p. 78]

62.  Experience Music Project, Seattle.  

                                    56

## [p. 79]

5.0    Design Proposal

                   The aim of this thesis, while attempting to develop an 

                   innovative way in which to create curvilinear struc-

                   turally supportive building skins, strives to provide 

                   a method of design that encapsulates the iterative 

                   design process from schematic design to fi nal con-

                   struction.  This means providing a novel way in which 

                   to design, document and build.  

                              57

## [p. 80]

5.1 Design Approach                                       concepts could be rapidly tested with mini-

                                                                                         mal investment of time while allowing down-

                               The design of a building requires the thought-            stream changes in the selected model to be 

                               ful integration of a rapidly expanding pal-               incorporated in a rapid and concise manner.  

                               ette of structures, systems and construction              This type of design is a partial possibility with 

                               approaches that if not considered early within            building information modeling (BIM); how-

                               and throughout the project can have deleteri-             ever its capacity is limited with regard to the 

                               ous effects when design changes occur down-               rapid changing of elements that are related to 

                               stream.  Current design practices treat many              each other.  In other words, necessary changes 

                               systems, such as mechanical, electrical or struc-         must be done on an element by element basis 

                               ture to name a few, as separate entities that             which, although translated into all of the rel-

                               are designed independent of one another and               evant drawings, fails to allow for rapid build-

                               occupy their own partitioned space.  While this           ing scale changes.  Parametric design allows for 

                               approach may be useful in relatively uncom-               this element relationship whereby changes to 

                               plicated spaces, its appropriateness begins               specifi c pre-defi ned parameters can infl uence 

                               to diminish when the complexity of building               any number of output variables.  

                               structure and layout begins to intensify.  At this 

                               point, a minor adjustment in one system may               The design component of this thesis utilizes an 

                               have dramatic effects on a neighboring system.            innovative program called Generative Com-

                               Additionally, when using drafting programs                ponents from Bentley Systems which is a pow-

                               that do not support a method for automatic                erful parametric, constraint-based modeler 

                               updating of documentation then all changes                capable of designing in the aforementioned 

                               require manual correction and update of rel-              manner.  While the program performs many 

                               evant drawings which again, with complex                  necessary functions and is able to generate a 

                               buildings, can result in mistakes, omissions and          variety of thesis objectives it is still under devel-

                               an increase in man hours.                                 opment and there are a number of additional 

                                                                                         requirements that are as of yet unavailable in 

                               Nature’s design process as stated in previous             the program but which will be addressed for 

                               chapters utilizes a number of feedback sys-               further research and development.  The key 

                               tems to direct the growth and formation of an             to success of the thesis will be an adherence 

                               organism based on the internal and external               to the philosophy of developing designs that 

                               forces acting on and within it.  All systems are          are not based solely on visually driven designs 

                               continually updated and act in concert with               but rather ones that include or are informed 

                               each other to provide optimum functionality               by intended modes of construction, the physi-

                               at all levels of development.  If this is applied to      cal characteristics of the materials to be used, 

                               architecture there arise possibilities to stream-         along with a biomimetic approach to spatial 

                               line the design process in that multiple design           and structural coherence.  This ‘bottom up’ 

                                                                                     58

## [p. 81]

development of architecture can be observed               morphologies, the physical limitations and 

                     in the attempt to create forms that are derived           benefi ts of the intended construction 

                     from higher-dimensional geometry, where sur-              materials, and the desired construction 

                     faces are defi ned in a strict mathematical sense         methods.

                     and contain the prerequisite of material com-

                     patibility during the manufacturing process.          At this point a number of questions are raised 

                     (Lalvani 1999, p32)                                   in order to arrive at the key products to be 

                                                                           realized at the end of the research.  These 

                     5.2      Design Objectives                            questions evolved from a critique of current 

                                                                           design approaches in a manner that elicits the 

                     Before delving into designs it is necessary to        possibilities for new outcomes.

                     defi ne some objectives for those designs and 

                     establish what it is that will be accomplished in     1.  Why are current methods of building 

                     their generation.  It is not a question of what           design and documentation ineffi cient?

                     is to be designed but rather what the design 

                     is to do and what can be derived from the                 a.   The relationship between element, 

                     design process that is of primary importance.                  system and building are often dis-

                     The signifi cance of this differentiation focuses              parate and multiple drawings are 

                     on design approach rather than design out-                     required to illustrate them.

                     come where the fi nal solutions have the ability          b.   Changes in the design are not easily 

                     to affect multiple design scenarios instead of a               propagated through the drawing set 

                     singular example.                                              which results in additional time and 

                                                                                    possibilities for error.

                     The two major objectives that form the basis              c.   The shift from sketch design to CAD 

                     for this thesis investigation are:                             development is a hard-edged thresh-

                                                                                    old in which abstracted and general-

                     1.   Develop a design process and documen-                     ized spatial and geometric ideas and 

                         tation system that allows the AEC (Archi-                  relationships are rigidized into a one 

                         tecture, Engineering, Construction) com-                   path directive.

                         munity to work more effectively as a cohe-            d.   Initial measurements must be 

                         sive unit with regard to the digital design                approximated which a priori neces-

                         and physical construction of architectural                 sitates later dimensional modifi cation 

                         projects.                                                  and ensures a built in time expendi-

                     2.  Create a variable structural prototype                     ture.

                         unit that is able to conform to a variety 

                         of complex surfaces and whose form is 

                         derived from natural spatial and structural 

                                                                       59

## [p. 82]

2.    Why are current methods for design and              more effectively organize the visual infor-

                                  construction of non-orthogonal surfaces              mation conveyed.

                                  and structures so much more diffi cult to       2.  Tailor the design and documentation 

                                  get built than linear surfaces and struc-            phase as more of a feedback oriented 

                                  tures?                                               method where minimal manual revisions 

                                                                                       are required to documentation when 

                                  a.  Complex surfaces and structures can              design changes occur.

                                      require many uniquely shaped ele-           3.  Devise methods of generating complex 

                                      ments to attain their three dimen-               surfaces that allow for elements that can 

                                      sional conformation, therefore devel-            be more easily designed and manufac-

                                      opment time and manufacturing                    tured.

                                      costs are elevated.                         4.   Create a system where the three dimen-

                                  b.  The construction documents and                   sional form of an element will specify its 

                                      actual process of construction can               location in the building with a minimal 

                                      be very complicated which requires               amount of measurement, positioning and 

                                      a highly skilled and knowledgeable               labor.

                                      workforce along with unique con-

                                      struction methods.                          5.   Select ideas that maintain the quality and 

                                  c.  Manufacturers are slow to adopt                  intent of the design while reducing the 

                                      new production methods that would                fi nal cost of the project.

                                      facilitate easier construction due to 

                                      the requirement that new produc-            5.4      Design Methodology

                                      tion and assembly methods as well as 

                                      the logistical systems would require        A structured approach to the genesis and 

                                      investment into new facilities and          development of the desired thesis objectives 

                                      their associated cost implications and      is necessary to allow for their broad relevance 

                                      risk.                                       to architectural constructions rather than their 

                             5.3      Design Requirements                         singular appropriateness for a given scenario.  

                                                                                  While this thesis seeks to provide exploratory 

                                                                                  physical manifestations of the design objectives 

                             From the above line of questioning it is pos-        it will also focus on developing an approach 

                             sible to arrive at a number of conclusions as to     and method to design, manufacture and con-

                             what schemes need to be developed and how            struction of architecture that will aid in pro-

                             they can be adapted to the design of complex         ducing more effi cient and cost effective build-

                             structural surfaces.                                 ings.

                             1.   Revise the current method of design doc-        Due to the nature of the investigations and 

                                  umentation and explore ways in which to         their development from natural systems it is 

                                                                               60

## [p. 83]

diffi cult and indeed undesired to separate their 

                          direction into discrete streams.  As a result, an 

                          overlapping of conditions will occur where 

                          the same biological infl uences will aid in the 

                          advancement of multiple design products.  

                          5.5        Design Drivers

                          With an idea of what is to be accomplished 

                          it is possible to look at natural systems that 

                          could begin to inform the design process.  The 

                          selected principles of biomimetics chosen in 

                          Section 3.2 are to be used as both inspiration 

                          for development of the thesis objectives as 

                          well as a yardstick by which to measure the 

                          appropriateness of the designs created.

                               1. Self Assembly

                               2.    The Power of Shape

                               3.    Resilience and Healing

                               4.    Materials as Systems

                               5.    Sensing and Responding

                                                                                         61

## [p. 84]

_(página sin capa de texto)_

## [p. 85]

6.0    Thesis Resolution

                   The advancement of the thesis takes place on a number of 

                   levels that build upon one another where conceptual design, 

                   development and construction strategies provide a base 

                   for the creation of structural building skin prototypes.  The 

                   fi rst design concept will focus on outlining a design pro-

                   cess that covers the entire range of an architectural project 

                   from schematic design to construction.  This process will be 

                   developed and rely upon nature’s methods of organization, 

                   instruction, and construction to provide a framework that 

                   will help to streamline the efforts in the Architecture, Engi-

                   neering and Construction (AEC) community.  The second 

                   and third design concepts will utilize knowledge gained both 

                   in the biomimetic design principles explored in Chapter 2 

                   as well as the organizational principles put forth in the fi rst 

                   design to create prototype scenarios for adaptive, curvilin-

                   ear, structurally-supportive building skins.

                              63

## [p. 86]

6.1      Design Concept #1 - Design                  instructions.  This scenario arises from physi-

                                       Methodology                                 cal limitations that exist in the natural environ-

                                                                                   ment.  Organisms must constantly compete 

                              The process of design proceeds along a path          for natural resources which can occur in lim-

                              from conceptual idea to fi nal physical form.        ited supply within an ecosystem and as such 

                              Although this is the preferred path for all par-     there arises and in-built need for both mate-

                              ties involved this is often not the case.  It is     rial and energy conservation.  This require-

                              inevitable that during the development pro-          ment exists not only for the formation of the 

                              cess a number of issues will arise that result       organism but for its continued survival.  The 

                              in changes to anything from minor details to         simplest set of instructions required to pro-

                              overall conceptual considerations.  So then, it      duce a viable organism is a necessity in that it 

                              would be benefi cial if the tools available for      reduces the physical size of the molecules that 

                              design were able to follow the lead of the           contain them.  Additionally, a reduction in the 

                              designer in that they allow for a freedom of         number of instructions automatically reduces 

                              controlled design exploration as well as the         the number of possible errors that can arise as 

                              ability to effectively document and describe         well as the investment of energy required to 

                              the fi nal form all the while utilizing a form or    correct them.  So then, it can be said that natu-

                              representation that can serve both equally.          ral organisms have through their development 

                                                                                   evolved informational and constructional sce-

                              The conception and development of the  narios that create maximal functionality from a 

                              design itself where a dynamic digital model          minimal investment of energy. 

                              that can adapt to specifi c environmental con-

                              ditions is favored over a static, unchangeable       Any attempt to reduce the complexity 

                              one that suits only the context into which it is     required for the realization of man made con-

                              placed and loses its adaptability in subsequent      structions can benefi t from an investigation 

                              projects.  While it is not expected that one         into how nature deals with its own architec-

                              design model will suffi ce for all subsequent        tural documentation and process of design.  To 

                              design explorations it is desired that a design      this end, it was at the molecular scale where 

                              scenario will arise in which discrete portions       the necessary directives were found.  The pro-

                              of a design may be brought together in differ-       cess whereby segments of DNA, which cells 

                              ent confi gurations to produce new and varied        transcribe into RNA and translate, at least 

                              morphologies without starting from a blank           in part, into proteins is able to contribute a 

                              slate each time.                                     number of ideas directly related to the way 

                                                                                   in which architectural documentation can be 

                              Some of the most technically and structurally        more effectively prepared and related to the 

                              intricate and emotionally evocative forms orig-      design of a structure.  

                              inate in nature from a relatively simple set of 

                                                                                64

## [p. 87]

6.1.1    A Natural Order                                 for full, functional development of an organ-

                                                                               ism are contained in its genetic code, the fi nal 

                      ‘Cells are inventive architects…To build these           form of the organism is directly infl uenced by 

                      elaborate structures…one can fi nd exam-                 the internal and external factors acting on and 

                      ples of any engineering principle in use today.          within it.  Diet, environment, physical stresses 

                      Fences are built, railways are laid, reservoirs          and a host of other factors infl uence the direc-

                      are fi lled, and houses are constructed com-             tion of growth and ultimately the fi nal out-

                      plete with rooms, doors, windows, and even               come.  Architecture and its creations are simi-

                      decorated in attractive colors.  Lap joints, but-        larly infl uenced by a set of developmental fac-

                      tresses, waterproofi ng, reinforcing rods, valves,       tors such as program, budget, siting, etc., that 

                      concrete, adhesives – each has a molecular               must all coalesce into a fi nal built form.  There 

                      counterpart.’  (Goodsell 1996, p81)                      is no absolute resolution to these factors, only 

                                                                               an attempt to best balance the necessities of 

                      Organisms carry within their genetic makeup              each so that the product approaches the ideal 

                      the instructions for complete self assembly.             or desired outcome.  Often times a variation 

                      The process of self assembly does not occur              in one of the factors infl uencing the design will 

                      in a vacuum however and the growth and fi nal            have implications whether positive or negative 

                      form of the organism is based on the static              for the entire collection.  A decrease in bud-

                      genetic sequence as well as the dynamic forces           get, for example, may require the reduction 

                      both internal and external which impose them-            or elimination of certain elements that are 

                      selves on the organism.                                  deemed non-essential.  

                      Section 2.1.1 DNA and Genetic Coding explained           If we are to envision the design process for 

                      how the genetic code is relatively defi cient            a building developing in this manner then it 

                      in the full complement of instructions that              will be benefi cial for reasons outlined above 

                      appear necessary to build complicated organ-             to reduce the number of instructions neces-

                      isms.  From this it was concluded that rather            sary for it to be designed and built.  This can 

                      than encoding for each cell separately there             be accomplished in both an informational and 

                      are a number of design principles that allow for         physical manner.  The key here is to reduce the 

                      development based on a set of growth param-              number of instructions required to defi ne the 

                      eters and strategies that reduce the complex-            building so that necessary changes or alterna-

                      ity of organic formation.  If this is the case, then     tive design scenarios can be executed with 

                      it follows that there is some innate fl exibility in     a minimal investment of time.  The physical 

                      the design outcome whereby the instructions              counterpoint to this is the utilization of natural 

                      in the set defi ne the parameters for develop-           design cues where the actual building elements 

                      ment rather than defi ning a rigid model for             are derived in such a manner that their three 

                      growth.  In other words, while the instructions          dimensional form helps to defi ne their loca-

                                                                           65

## [p. 88]

tion and connection within the building thus        tion of multiple elements.  Here, the graph is 

                             reducing the number of instructions required        still directed in that the relationships proceed 

                             for its proper construction.  The method for        from independent upstream nodes to depen-

                             natural development and assembly outlined           dent downstream nodes yet it provides a much 

                             below will help in creating a framework for         freer approach to the relationships established 

                             man-made design, manufacture and construc-          between components.  See Figure 64.

                             tion techniques in line with a design process 

                             utilizing a minimum number of instructions.         The design process as it relates to use, layout, 

                                                                                 structure and construction is often quite com-

                             Section 2.1.4 Hierarchy of Structure illustrated    plex and requires a number of iterations to 

                             how patterns are intrinsic to natural systems       arrive at a viable fi nal design.  Often, the pro-

                             in that every component must not be looked          gressive development of these design itera-

                             at as an individual unit but as part of a collec-   tions will occur with digital models that have 

                             tive whole.  While treating the entire building     been translated into physical models for hands 

                             as a complete unit may be a diffi cult task, the    on manipulation and then digitized back into 

                             idea begins to clarify itself when we start to      the computer for further development.  While 

                             examine the various ways in which this may          this process does work quite well it has the 

                             be possible.                                        drawback of not being backwards compatible, 

                                                                                 that is, once the design is changed in the physi-

                             A benefi t with regard to design development        cal model and digitized back into the computer, 

                             or alteration that can be derived from Section      the previous digital model becomes redundant.  

                             2.1.4 Patterns arises if the design approach is     By infusing the project with an approach that 

                             looked at as a hierarchical organization.  Typical  parameterizes the relevant design variables, 

                             tree diagrams representing informational hier-      changes that may be necessary, whether they 

                             archies proceed in a strict additive or reduc-      be structural or aesthetic, have the ability to 

                             tive manner where one parent node will spec-        be changed within the digital model.  A model 

                             ify many children nodes or vice versa.  See Fig-    with parameterized design variables has the 

                             ure 63.  While these methods of organization        benefi t of reducing the amount of remodeling 

                             are useful in their respective contexts such        that is necessary for each design iteration.  In 

                             as hierarchical transforms or feature trees in      fact, each modeling instruction or set of instruc-

                             solid modeling applications, their effective-       tions can, like a gene in natural organisms, be 

                             ness diminishes when applied to the process         turned of or on to express or hide its function.  

                             of design itself.  In real world design scenarios   Changes to the design parameters are thus 

                             there may be instances where a node or par-         reversible and time is not lost if a previous 

                             ticular design element will require input from      design direction is to be revisited.  It should be 

                             a variety of upstream sources for its defi ni-      noted however, that the model must be prop-

                             tion and it in turn may infl uence the defi ni-     erly developed so that any modeling instruc-

                                                                              66

## [p. 89]

tion that is turned off will either have a corol-

                   lary to takes its place, or that its absence will 

                   not result in downstream errors.  Any results 

                   obtained from analysis of the model by other 

                   related design disciplines that require a change 

                   in the design would be quickly expressed and 

                   tracked in the program code.

                   6.1.2   The Relevance of Parametric 

                           Design

                   CAPD (Computer Aided Parametric Design), 

                   as it is referred to for the purpose of this dis-

                   cussion, can begin to emulate the natural pro-

                   cess of growth and development by allowing 

                   relationships between design variables to be     63.  Tree diagram showing typical hierarchical relation-

                   created so that they can infl uence each other   ship. for solid modeling operations.

                   according to prescribed methods of interac-

                   tion.  In this way the design is able to respond 

                   to manipulation of parameters that coincide 

                   with developmental forces driving the design.  

                   A closed feedback loop is created for model 

                   generation, sequencing, alteration, visualization 

                   and construction that effectively overcomes the 

                   inherent inability in the majority of CAD soft-

                   ware to do the same.  This feedback enables the 

                   designer to reduce time in varying and in turn 

                   manually revising changes in the design.  Addi-

                   tionally, and in keeping with evolutionary the-

                   ory, albeit on a condensed timeframe, CAPD 

                   allows for the simultaneous development of 

                   multiple designs within the same model with 

                   the possibility for selection of the most appro-

                   priate once they have all been examined.  This 

                   type of parametric design enables the designer 

                   to create dependencies (relationships) any-      64.  Tree diagram showing a composite hierarchical 

                   where within the model and between design        approach.

                                                                 67

## [p. 90]

components.  The size of a duct shaft may be            ric design system quickly becomes apparent 

                               dependent on the area of the fi rst fl oor which        when it is realized that both the fi nal form and 

                               is in turn dependent on the number of fl oors           the subcomponents are variable.  

                               that are proposed for the building.  Alterna-

                               tive parametric approaches exist albeit on a            6.1.4 Generative Components

                               more simplifi ed level where relationships exist 

                               between components that physically interact             6.1.4.1 An Outline

                               with each other as with walls and windows 

                               for example.  If the wall is moved the window           This thesis makes use of a parametric digital 

                               will move with it.  An ideal parametric design          design system called GenerativeComponents 

                               system would effectively encapsulate both the           (GC) by Bentley Systems Incorporated that 

                               broader project sized parametric associations           runs in their Microstation design environment.  

                               and the more specifi c building component               The unique character of GC arises from its 

                               relationship methods.                                   ability to allow for and promote extremely 

                                                                                       customizable parametric and associative 

                               6.1.3 Parametric Correlation                            design solutions.  Parametric design in this 

                                                                                       case refers to a method of design that estab-

                               With a parametric digital design system an              lishes dependencies or associations between 

                               issue arises between bottom-up and top-                 design elements.  This means that the behavior 

                               down design styles.  The bottom-up method               of specifi c components of a design whether 

                               contains within it some vision of the overall           they are walls, cladding panels or structural 

                               project design and seeks to resolve this design         columns, are defi ned such that changes that 

                               through a gradual development and integration           occur in the design infl uence not only the ele-

                               of building elements into a larger whole.  The          ment that is altered but all of the elements 

                               top-down method approaches the design in a              that are associated with that element.  While 

                               different light where there is an initial develop-      the individual design components may range 

                               ment of the whole scheme with subsequent                from a simply defi ned layout point based on 

                               subdivision into its appropriate subcompo-              Cartesian coordinates to a complex array of 

                               nents.  A composite approach to design would            trusses that adapt to localized roof conditions, 

                               most likely be required in that to effectively          it is in their user defi ned associations to one 

                               establish a set of hierarchical component rela-         another that makes GC parametric design 

                               tionships it is necessary to have an idea of the        so powerful.  The designs created in GC are 

                               fi nal product.  However, it is diffi cult to model     dynamic instruction sets that are developed 

                               an approximate fi nal form without fi rst defi n-       with an understanding of what the end result 

                               ing the parameters that allow for sequential            is to be without the need to have this vision 

                               variation and the building of components from           fully realized.  The parameters and associations 

                               the bottom up.  The usefulness of a paramet-            that are defi ned within and between compo-

                                                                                   68

## [p. 91]

nents allows for a variability of design scenar-           ogy from concept genesis to design develop-

                       ios based on the conscious implementation                  ment to rapid prototyping and digital fabrica-

                       of these by the designer.  In contrast to stan-            tion to the fi nal export and management of 

                       dard 2D and 3D design programs that cre-                   construction documentation all of which are 

                       ate static models and require a large input of             instantaneously variable and updateable.   

                       time to explore and implement variations, GC 

                       is able to rapidly incorporate these changes               6.1.4.2 Programmatic Description

                       into the existing model being used while still 

                       maintaining the full functionality of the previ-           In order to fully understand the usefulness and 

                       ous iteration if it is to be revisited in the future.      applicability of GC with regard to this thesis it 

                       Additionally, GC allows for a scalability of com-          is necessary to outline the way in which the 

                       plexity with regard to the clarity of the design           GC environment is organized and used.

                       at any point within the process.  Early on in 

                       a project when many variables are unknown                  GC is based on the creation of dependency 

                       GC is able to create a framework that allows               relationships between individual design com-

                       for an exploration of design intentions with-              ponents where the output variable for one 

                       out defi ning these intentions in a rigid manner.          is related to the input defi nition of another 

                       If one or any number of the design param-                  and any changes that occur in the former 

                       eters need to be revised then they will be                 will propagate to all of its associated down-

                       instantly updated and these changes will prop-             stream dependent components.  The hierar-

                       agate through the model to align it accord-                chical structure that develops from these rela-

                       ingly.  When the project has developed to a                tionships forms what is known as a directed 

                       point where an increased desire for geomet-                graph.  The graph contains within it all of the 

                       ric accuracy is required, then it is possible to           dependencies between the associated com-

                       do so with minimal input.  While GC allows                 ponents.  GC displays this graph in a symbolic 

                       for a high degree of freedom with regard to                model view which is very useful for allowing 

                       design exploration and fi nal solutions it should          the designer to see a graphical representa-

                       be noted that the amount of fl exibility inher-            tion of typically non-visual relationships as well 

                       ent within the design is a function of the way             as providing a tool that allows for others to 

                       in which the designer has created the model.               quickly become familiar with the design intent 

                       The program itself becomes most useful when                and relationships.  See Figure 65.

                       the designer is able to logically establish a 

                       design hierarchy that is variable based on their           The components used in GC are able to exhibit 

                       intuition and the requirements or restrictions             multiple behaviors in that their input defi nition 

                       imposed by the chosen method of manufac-                   can vary depending on the desired function 

                       ture and construction.  GC is able to play a key           of the component.  In this case a single point 

                       role in each step of current design methodol-              may defi ne the preliminary layout position for 

                                                                              69

## [p. 92]

the excavation of a building and may be based         programming language (which is automatically 

                              on the input of specifi c Cartesian coordinates       generated from the transactions) any part of 

                              while another point may represent the start-          the fi le from the addition of new features to 

                              ing position for a cladding panel on a curvi-         the rearrangement or consolidation of specifi c 

                              linear surface whose position is defi ned by          features.  This ability allows the designer to 

                              the intersection of structural elements.  It is       move between conventional graphically based 

                              important to note that the designer can effec-        design into the realm of scripting and pro-

                              tively change the input variables by which the        gramming.  The benefi t of this fl exibility is that 

                              point is derived without altering or infl uencing     it allows for the development and implemen-

                              the downstream dependency structure of the            tation of new components over and above the 

                              components that are associated with it.  See          current palette of features contained within 

                              Figure 66.                                            the base program.  

                              Both the directed graph and the symbolic view         6.1.4.3 Terms

                              are generated through actions initiated by the 

                              designer.  These actions are performed through        In this section a number of the key terms 

                              the defi nition of new features or design steps.      used throughout the GC design system will be 

                              New features may contain the addition or vari-        defi ned in order to aid in the understanding of 

                              ation of one or many individual components.           subsequent writings.  (Aish 2004)

                              Once the desired amount of modifi cation to 

                              the model has been added then the new steps           Component Type – Refers to the collection 

                              are recorded as transactions.  The sequence of        of input and output properties and their asso-

                              transactions is recorded in a transaction fi le as    ciated update methods (explained below) as 

                              program code and in a transaction view that           they relate to a specifi c geometric element or 

                              graphically displays them.  The importance of         collection of elements that comprise a build-

                              the transaction view is that it effectively dis-      ing component.

                              plays for the designer a historical visual rep-

                              resentation of the design progression as well         GC already includes a large collection of pre-

                              as containing within it the necessary informa-        defi ned components that include but are 

                              tion to allow the program to build the model.         not limited to; Point, Line, Arc, BsplineCurve, 

                              See Figure 67.  The user can step backward            BsplineSurface, Solid and modeling operations 

                              and forward sequentially through the design to        that allow for the creation of additional com-

                              revisit any feature that was created to deter-        ponents.

                              mine its effectiveness, relevance or any other 

                              number of design questions.  The transaction          Component Instance – The component 

                              view is directly linked to the transaction fi le      instance refers to the actual usage of a specifi c 

                              so that a user is able to open, view and edit in      component type in a particular feature of the 

                                                                                70

## [p. 93]

_(página sin capa de texto)_

## [p. 94]

The values for these properties are defi ned by 

                                                                                               an expression that satisfi es the requirements 

                                                                                               for their input.  

                                                                                               Property expression – This is the form of the 

                                                                                               input for the update method by which a prop-

                                                                                               erty value is arrived at.  GC is able to accept 

                                                                                               a variety of property expressions from some-

                                                                                               thing as simple as a single integer input to 

                                                                                               something more complex like a mathemati-

                                                                                               cal formula derived from the interaction of 

                                                                                               the property values from other component 

                                                                                               instances.

                                                                                               For example, a circle whose radius is defi ned 

                                                                                               by the property Circle01.Radius has the ability 

                                  67.  GC transactionFile view                                 to contain a variety of expressions such as

                                                                                               Circle01.Radius = 5

                                                                                               Circle01.Radius = Line01.Length*5

                                                                                               Property Value -  The property value repre-

                                                                                               sents the result of the latest recalculation of 

                                                                                               the property expression.

                                                                                               Graph Variable – A graph variable can be cre-

                                                                                               ated that defi nes a value for use within the 

                                                                                               property expression of a component or any 

                                                                                               number of components.  By changing the value 

                                                                                               of the graph variable all of the components 

                                                                                               associated with it will recalculate their values.

                                                                                               For example, a graph variable called line_

                                                                                               length can be created that defi nes the length 

                                                                                               of Line01 from the previous example.  The 

                                                                                               va

## [p. 95]

ment, or a string.  If the value of the graph vari-     When the initial design of a building is tak-

                     able was set to 5, then the Circle01.Radius =           ing place there are often a large number of 

                     Line01.Length*5 expression would result in a            variables that are unfi xed and changeable.  By 

                     value of 25.                                            carefully planning the strategy for the devel-

                                                                             opment of the building concept it becomes 

                     Dependencies (Associations) – GC maintains              possible for the model to develop in a way 

                     dependencies between features within the                that allows for relative freedom with regard 

                     drawing.  Simply stated this means that when            to dimensioning.  As the building develops the 

                     defi ning a new feature the user has the abil-          dimensions can be updated to refl ect the fi nal 

                     ity to associate its position or any number of          requirements. 

                     characteristics with any other feature or set 

                     of features in the drawing.  If the parent fea-         When the GC program loads it runs within 

                     ture is updated then any children features that 

                     are associated to it will automatically update          the Bentley Structural design program.  The 

                     themselves based on the user defi ned depen-            GC Graphical User Interface (GUI) appears as 

                     dencies.  We can use the length of a line as an         a fl oating window that can be repositioned as 

                     example here where the line represents the              desired.  In it are contained all of the functions 

                     length of a wall.  We are able to defi ne a num-        provided by GC.  Running behind the GUI is a 

                     ber of points along this line that represent the        palette of user defi ned windows that are able 

                     position of potential vertical structural mem-          to display both the symbolic view as well as 

                     bers.  If the length of the wall is to be length-       multiple graphic views of the 3D model.  See 

                     ened then GC will automatically change the              Figure 68 & 69.

                     position of the vertical members to satisfy 

                     the relationship to the line that the user pre-         The premise for the symbolic view is to rep-

                     defi ned.  At any point however, the user has           resent the computer model in a way that illus-

                     the ability to change the dependencies if they 

                     require alteration.  At this point the fi le will       trates the dependencies that can exist between 

                     recognize the changes and alter the form of             different features.  Each feature is represented 

                     the model accordingly.                                  by a circle with a defi ning tag within it.  Con-

                                                                             nectors join features that have relationships to 

                     6.1.4.4 An Illustrative Example of the                  each other.  In a traditional CAD program an 

                               Generative Components System                  element, such as a line, is drawn from point 

                                                                             to point but the line and points do not main-

                     This relatively simple example will help to             tain a relationship to each other.  The points 

                     demonstrate the visual and programmatic                 or line may be moved while leaving the others 

                     platform of GC.  In this case a building will be        unchanged.  It is the coordinates of the ele-

                     developed with a variable footprint, number of          ments that are recorded in these “non-asso-

                     fl oors, and fl oor height.                             ciative” CAD programs not their relationships 

                                                                             to one another.  In a project where design 

                                                                         73

## [p. 96]

changes can affect multiple drawings, tradi-           as a representation of its associativity to other 

                              tional CAD programs are unable to update               components in the fi le, and in the GUI trans-

                              them automatically because they elements               action view as steps in the transaction list 

                              within them are not associated with each               which represent the design history.  See Figure 

                              other.  At this point the user must use a great        72.  Lines representing the length and width 

                              deal of time in checking and cross-referencing         of the building can be constructed next.  The 

                              drawings for accuracy.  If changes occur fre-          lines will be dependent upon Point01 and the 

                              quently then it is possible to see where a great       baseCS.  The fi rst Line01 is a line ByStartPoint-

                              deal of time can be lost.  The drawings pro-           DirectionAndLength which uses the GV Build-

                              duced from a GC model are associated and               ing_Length as the property expression for its 

                              thus any changes that occur will instantly be          execution. See Figure 73.  The length of the 

                              propagated to all relevant drawings.                   building is now parametrically dependent on 

                                                                                     the value contained within the GV.  Any time 

                              1)  Defi ning the graph variables                      the building length needs to be changed it can 

                                                                                     be done quickly by sliding or manually input-

                              A graph variable is created by selecting add in        ting a new value into the Building_Length GV.  

                              the GV view, defi ning the name of the new GV 

                              then inputting the desired output value and            Consider, for sake of proportion, that the 

                              value limits if required.  See Figure 70.              width of the building is desired to be one half 

                                                                                     its length.  It is possible then to defi ne the value 

                              2)  Developing the model                               for the Building_Width as Building_Length*0.5.  

                                                                                     Having originally set the value for the Build-

                              Once the GVs have been defi ned it is possible         ing_Width as a default value of 10 the change 

                              to begin creating features that will visually rep-     that is made to it will add another transac-

                              resent the building design.  A base Point01 is         tion statement.  Each transaction statement is 

                              defi ned that corresponds to the primary lay-          given a default name of Graph Changed By User 

                              out point of the building.  This point is defi ned     which is editable for the user to defi ne the 

                              choosing from a number of Point instances, in          actions taken in that transaction.  If for some 

                              this case a point ByCartesianCoordinates that          reason the user wishes to unlink the building 

                              uses the base coordinate system baseCS as its          length and width then it is possible to suppress 

                              input coordinate system and X,Y,Z values of            the change by right-clicking on it and selecting 

                              0 (null) to place the point within the baseCS.         suppress.  This will change the GV value back 

                              See Figure 71.                                         to its original state.  See Figure 74.

                              Point01 is now defi ned in a number of areas           Line02 will be defi ned in the same manner as 

                              within GC.  It appears in the graphic view as          Line01 however it will use the newly edited 

                              a graphic representation, in the symbolic view         Building_Width GV as its property expres-

                                                                                  74

## [p. 97]

sion.  Now that both lines have been defi ned 

                     they can be played in the transaction fi le and 

                     they will now appear in both the symbolic and 

                     graphic views.  In the symbolic view it is pos-

                     sible to see in graphic form the logical associa-

                     tivity of the developing model.  The baseCS is 

                     situated at the top with Point01 and Line01 

                     and Line02 directly associated with them.  The 

                     GV Building_Length is associated with Line01 

                     and Building_Width.  The Building_Width is 

                     associated only with Line02.  See Figure 75.

                     As the model and transaction fi le develop the 

                     symbolic view will develop alongside them 

                     to aid the user in keeping track of the logical 

                     order in which the design is progressing.  The 

                     next step is to defi ne the opposing lines defi n-

                     ing the length and width.  This is done by off-

                     setting a new child line that is associated with 

                     the values of the parent.  At this point all of the 

                     lines are dependent on the Building_Length 

                     GV for their defi nition.  See Figure 76.             68.  GC Graphical User Interface (GUI)

                     To add the lines representing the four verti-

                     cal corners of the building it is possible to do 

                     so by defi ning their origin points as the end 

                     points of the plan lines.  This will allow the ver-

                     tical lines to realign themselves if a plan change 

                     is made.  The feature used is a line ByStart-

                     PointDirectionAndLength but the uniqueness 

                     here lies in the defi nition of the origin point 

                     which is not a single point but three of the 

                     planar end points and Point01 thus creating 

                     four lines.  This allows one feature to create 

                     four lines all editable with one variable.  In this 

                     case the length expression is defi ned by the 

                     Floor_Height GV multiplied by the Number_             69.  GC Symbolic view and Model view

                                                                        75

## [p. 98]

of_Floors GV.  It is possible to see here from 

                                                                                                      the symbolic view how Line05 is directly asso-

                                                                                                      ciated with a number of other components 

                                                                                                      and that the defi nition of Line05 which repre-

                                                                                                      sents four physical lines in the building model is 

                                                                                                      defi ned by the property expressions of those 

                                                                                                      other components.  See Figure 77

                                                                                                      The fi nal portion of the exercise is to defi ne 

                                                                                                      the individual fl oors and the roof which is 

                                                                                                      completed in two steps.  The lines defi ning the 

                                    70.  Defi nition of Graph Variables.                              building width are created by a Line ByOffset 

                                                                                                      from the ground plane by a distance equal to 

                                                                                                      the Floor_Height GV and the number of offset 

                                                                                                      lines describing the fl oors and roof is generated 

                                                                                                      by the Number_of_Floors GV.  These opera-

                                                                                                      tions can be seen below in the GC Script Edi-

                                                                                                      tor which allows one to view the programming 

                                                                                                      code that GC creates as the user develops the 

                                                                                                      model in the transaction view.  See Figure 78.  

                                                                                                      The series property expression allows for a 

                                                                                                      number of sequential values to be obtained 

                                                                                                      through defi ning a lower and upper value that 

                                                                                                      is divisible by a third value.  For example, the 

                                                                                                      following Series(0,5,1) would result in output 

                                                                                                      values of 0, 1, 2, 3, 4, 5.

                                                                                                      3)  Refi ning the model

                                                                                                      Once the GC script has been played through 

                                                                                                      the fi nal result can be viewed in a number of 

                                                                                                      different ways according to the desired inter-

                                                                                                      pretation.  The model view demonstrates the 

                                                                                                      physical condition, the symbolic view displays 

                                                                                                      the hierarchy of relationships and associations 

                                                                                                      between building elements, the transaction 

                                    71.  Defi nition of Point01.                                      view lists the historical order of operations 

                                                                                                 76

## [p. 99]

used to obtain the product and the GCScript 

                     Editor shows the source code that can be fur-

                     ther manipulated by the user.  See Figures 79-

                     82.

                     The fi nal model produced here although sim-

                     ple in its geometric layout is very robust with 

                     regard to its instantaneous variability with rel-

                     atively minor user input.  With manipulation 

                     of just three numbers it is possible to vary 

                     the length, width, fl oor height, and number of 

                     fl oors within the building.  The different model     72.  Point01 in the Symbolic, TransactionFile and Model 

                     confi gurations realized in the following images 

                     were all created in less than one minute total 

                     time.   See Figure 83.

                     4)  Management and Export of Model for 

                     Construction

                     From this model a number of additional oper-

                     ations can be performed that streamline the 

                     AEC process.  These can include fabrication 

                     planning for export to Computer Numerical 

                     Control (CNC) manufacturing, model proto-

                     typing, drawing extraction for setup of con-

                     struction drawings, among others.  Depend-

                     ing on the values assigned to the model the 

                     export products can be similarly used for 

                     physical models or full scale production.  At 

                     the writing of this thesis however, not all of 

                     these additional operations are functional in 

                     GC.

                                                                           73.  Defi nition and property expression for Line01.

                                                                       77

## [p. 100]

6.1.5   Parametric Modeling Based on 

                                                                                    the Biological Genome

                                                                            William Lethaby writes in his Architecture: an 

                                                                            Introduction to the History and Theory of the Art 

                           74  Graph Variable Building_Width changed.       of Building from 1911 that “[s]ome day we shall 

                                                                            get a morphology of the art by some architec-

                                                                            tural Darwin, who will start from the simple 

                                                                            cell and relate it to the most complex struc-

                                                                            ture.” 

                                                                            Genomic Background

                                                                            All living organisms contain DNA which is a 

                                                                            nucleic acid that contains the genetic instruc-

                                                                            tions specifying the biological development of 

                                                                            all cellular forms.  The DNA molecule is com-

                                                                            posed of a vast sequence of nucleotide bases 

                                                                            arranged into chromosomes which represent 

                           75  Symbolic view of component dependencies.     physically separate molecules.  Each chro-

                                                                            mosome contains genes which are the prin-

                                                                            cipal physical and functional units of hered-

                                                                            ity.  Genes themselves are specifi c sequences 

                                                                            of nucleotide bases that encode instructions 

                                                                            for the manufacture of proteins.  It is the pro-

                                                                            teins that execute most biological functions 

                                                                            and comprise the majority of cellular struc-

                                                                            tures.  Proteins are large molecules composed 

                                                                            of smaller amino acid subunits.  Unique chemi-

                                                                            cal properties characterize the twenty differ-

                                                                            ent amino acids and it is these properties that 

                                                                            cause the protein molecule to fold itself into 

                                                                            various three dimensional structures that per-

                                                                            form a particular function within the cell.

                                                                            The amalgam of all proteins in a cell is referred 

                           76  Offset of Line03 from Line01.                to as a cellular proteome.  The entire collec-

                                                                         78

## [p. 101]

tion of all cellular proteomes in an organ-

                    ism is referred to as the complete proteome.  

                    While the genome is relatively unchangeable, 

                    the proteome is quite dynamic and undergoes 

                    constant changes in response to numerous 

                    intra- and extra-cellular environmental infl u-

                    ences.  The chemistry and behavior of a pro-

                    tein is derived from the static gene sequence 

                    and by the infl uence of other proteins in the 

                    cell which it encounters and with which it 

                    reacts.

                    The process of creating a protein from a 

                    segment of DNA is one that follows a path 

                    from informational to physical.  A sequence of 

                    instructions creates a physical molecule.  If we 

                    delve a little deeper into how this mechanism 

                    operates certain rules develop that can be rel-

                    evant to architectural design practices.             77.  Symbolic view of model and dependencies for 

                                                                         Line05.

                    Erwin Schrodinger, the famous physicist, pub-

                    lished a book in 1944 entitled What is Life?  In 

                    his book he posited that chromosomes con-

                    tained what he referred to as the “hereditary 

                    code-script” of life.  He noted however that 

                    “…the term code-script is, of course, too nar-

                    row.  The chromosome structures are at the 

                    same time instrumental in bringing about the 

                    development they foreshadow.  They are law-

                    code and executive power – or to use another 

                    simile, they are architect’s plan and builder’s 

                    craft – in one.”  He envisioned the dualistic 

                    nature of these elements to be intertwined in 

                    the molecular structure of the chromosomes.  

                    Through an understanding of the molecular 

                    structure it was then possible to understand         78.  View of GC Script Editor and relevant programming 

                    both the “architect’s plan” and the eventuality      code.

                                                                     79

## [p. 102]

produced through the “builder’s craft.”   (Sch-

                                                                                         rodinger 1944)

                                                                                         DNA – The nucleotide sequence is relatively 

                                                                                         fi xed and unchangeable containing within it all 

                                                                                         of the instructions to build an organism.  As 

                                                                                         noted previously the number of cells con-

                                                                                         tained within the human body is 10,000 times 

                                                                                         greater than the number of instructions con-

                                                                                         tained within the DNA sequence.  The human 

                                                                                         genome therefore has developed ways in 

                                                                                         which to produce an incredibly complex form 

                                                                                         from a comparatively small instruction set.  

                                                                                         When a project is ready for construction the 

                                                                                         design documentation and digital models for 

                                                                                         the project must be able to fully explain and 

                                                                                         instruct all parties involved as to how it will 

                               79.  Symbolic view of component dependencies.             be constructed.  Ideally it would be preferred 

                                                                                         to have one CAD database that could handle 

                                                                                         every aspect of the project including visualiza-

                                                                                         tion, documentation, structural and material 

                                                                                         optimization, and export for manufacturing.  

                                                                                         Although a large amount of planning and orga-

                                                                                         nization is quite helpful in carrying a project 

                                                                                         along it is in the approach to design and the 

                                                                                         design itself where novel methods lead to effi -

                                                                                         cient outcomes.  Taking inspiration from natu-

                                                                                         ral reductive instructional and generative tech-

                                                                                         niques as outlined in Chapter 2, such as pat-

                                                                                         terning, bilateral symmetry, multiplicity of func-

                                                                                         tion, size correlation and inbuilt redundancy it 

                                                                                         becomes possible to reduce the complexity of 

                                                                                         architectural design at its outset.  The approach 

                                                                                         to a design and its realization should be viewed 

                                                                                         as a logical progression where steps taken to 

                               80.  TransactionFile view                                 reduce the complexity of the design process 

                                                                                     80

## [p. 103]

81.  GCScript Editor

         82.  Model View.             83.  Symbolic view of component dependencies.

                                81

## [p. 104]

early on will greatly reduce the complexity of         these contributors can be thought of as chro-

                              the design product in the later stages.                mosomal constituents.  Rather than all work-

                                                                                     ing collectively the various groups involved 

                              Chromosomes – Segments of DNA contain-                 would be able to work independently on ful-

                              ing different instruction sets.  If the complete       fi lling their own requirements yet still contrib-

                              DNA sequence were to be physically laid out            ute effectively to the fi nal form of the proj-

                              in a line it would measure approximately two           ect.  It would become unwieldy if every group 

                              meters in length. (McGraw 1999)  Obviously             involved in the project was required to work 

                              this incredible amount of information can              from the whole digital model.  The fi le size and 

                              become unwieldy if there is not an effi cient          complexity of this model would quickly grow 

                              way to organize and utilize it.  In this manner        too large for effi cient utilization.  Different sec-

                              the genomic information is separated into a            tors of the AEC community utilize different 

                              number of chromosomes containing a differ-             programs for developing and analyzing their 

                              ent subset of the complete DNA sequence                designs.  A complex 3D model developed by 

                              with each being responsible for producing a dif-       an architect often contains extraneous infor-

                              ferent set of functional products.  The division       mation which is not required by the struc-

                              of instructions also allows the cellular mecha-        tural engineers who as a result must resort to 

                              nisms to perform a number of processes on              building their own more simplifi ed structural 

                              individual chromosomes all the while main-             model.  Ideally then, the building information 

                              taining the full DNA sequence and full func-           contained within the digital database would 

                              tionality of the cell.  All of the chromosomes         exist on multiple levels of granularity so that 

                              are contained within the nucleus of the cell           each discipline could work effectively with it.  

                              as a unit.  See Figure 84.  This image illustrates     Each design discipline would view and work 

                              a unique method for the visualization of the           with the model and  the elements within it at 

                              chromosomes and hence the discrete infor-              the required level of complexity in that only a 

                              mational units of the genome where levels              subset of the total building information would 

                              of detail emerge depending on the required             be visible.  A beam for example may depend-

                              depth and detail of information.                       ing on its immediate graphical or analytical 

                                                                                     function be represented as a solid model for 

                              An architectural project must utilize the knowl-       assembly, a fi nite line element for structural 

                              edge and resources of a number of different            analysis, as source code for CNC operations 

                              specialists like engineers, HVAC or daylighting,       or as a pure graphic for rendering purposes.  

                              that help to develop specifi c areas of the design     The equivalent representation from biological 

                              for incorporation into the fi nal product.  If we      modeling can be seen in Figure 85.

                              envision a digital system for the effective man-

                              agement of the enormous information being              As a subset of the architectural portion of the 

                              delivered by a variety of sources then each of         design it is here that GC fi rst comes into play.  

                                                                                  82

## [p. 105]

The program itself represents the opportu-

                     nity for import/export to a number of other 

                     design and analysis programs as part of a large 

                     feedback loop.  Depending on user input and 

                     the defi nition of new components, the GC 

                     design system is able to be refi ned for future 

                     use.  In this regard GC essentially goes through 

                     one generation of development every time a 

                     new component(s) is/are created.  Over time 

                     the program will grow in its ability to cater to 

                     the individual complexity associated with the 

                     various disciplines and fi rms that use it.  At the 

                     same time there is an inbuilt capability of GC 

                     that allows individual components from differ-

                     ent versions of the program to be exchanged 

                     if desired.   

                     Genes – Each chromosome is further subdi-

                     vided into a number of genes that are each 

                     responsible for encoding for individual pro-

                     teins.  This subdivision however exists on an         84.  24-Color 3D FISH (Fluorescence in situ hybridiza-

                     informational level as the genes are all con-         tion) Representation and Classifi cation of Chromo-

                                                                           somes in a Human G0 Fibroblast Nucleus

                     tained within the physical chromosome.  This 

                     is the smallest informational unit within the 

                     genome that contains the instructions neces-

                     sary for the production of a functional physical 

                     unit that aids in carrying out all of the functions 

                     within the human body. 

                     If the chromosome represents each discipline 

                     involved in the progressive design of a proj-

                     ect then the gene represents the information 

                     developed by and contained within these dis-

                     ciplines.  The designs that they develop repre-       85.  Protein model showing varying levels of amino acid 

                     sent the transition from practice to implemen-        detail from left to right.

                     tation.  As such the strategies used in this area     A)  Hydrogen bonding in alpha-helix backbone

                                                                           B)  Image with additional side chains 

                     are crucial in establishing a closed feedback         C)  Electron density image

                                                                       83

## [p. 106]

system that is essential for a proper design to        tural or mechanical roles, such as those that 

                              progress from design to construction.  At this         form the struts and joints of the cytoskeleton 

                              point the idea becomes craft.                          or those serving as biological scaffolds for the 

                                                                                     mechanical integrity and tissue signaling func-

                              All of the components contained within GC              tions. 

                              can be likened to the genes that enable an 

                              organism to be developed.  Just as there are           A protein is the functional manifestation of 

                              multiple alleles for eye color or hair color so        a polypeptide gene product where individ-

                              too does a GC Point or other component                 ual instances are assembled to create the 

                              contain multiple update methods that allow             fi nal building form.  It should be noted how-

                              for unique geometric confi gurations.  The pro-        ever that a functional protein may arise from 

                              grammatic genotype defi nes a specifi c phe-           a single polypeptide in its tertiary structure or 

                              notype and it is useful here to note that the          from the assembly of two or more polypep-

                              expression of the phenotype is related to the          tides into a quaternary structure.  Protein con-

                              interaction of the polypeptide gene products           struction proceeds along a path from primary 

                              and the environment.  This is one of nature’s          to quaternary structure with increasing mor-

                              ways of allowing for diversity while still main-       phological complexity attained in each phase.  

                              taining a fi xed number of instructions.  See Fig-     Like the process of DNA to protein, so too 

                              ure 86.  Accordingly, the physical results rely on     does the four stage development of the pro-

                              both the relatively static instruction set as well     tein itself proceed from informational repre-

                              as the fl uid infl uences imposed by the variabil-     sentation to physical manifestation.  

                              ity of environmental stresses.  So too then it 

                              is useful if the digital environment can utilize a     Primary Structure – The covalently bonded 

                              logical and ordered design palette that deliv-         structure of the molecule.  This includes the 

                              ers multiple results based on unique combina-          sequence of amino acids, together with any 

                              tions of components.  There are a number of            disulfi de bridges.  All the properties of the fi nal 

                              ways a point or surface can be derived, Figure         protein form and function are determined, 

                              87, but it is in the way that the components           directly or indirectly, by the primary struc-

                              associate with each other that infl uence how          ture.  Any folding, hydrogen bonding, or cata-

                              they behave.  In this way a simple set of com-         lytic activity depends on the primary structure.  

                              ponents can defi ne a complex array of con-            See Figure 88.

                              structions.

                                                                                     Primary Structure in Practice – The aim here 

                              Proteins – Complex molecules made up  is to begin developing a framework upon 

                              of amino acid subunits.  Many proteins are             which the design and subsequent alteration of 

                              enzymes or subunits of enzymes, catalyzing             a building and its structure can be carried.  

                              chemical reactions. Other proteins play struc-         If the development of a design model in the 

                                                                                  84

## [p. 107]

digital environment is to be useful in all stages 

                    of the design then it must be constructed in a 

                    logical manner that can be understood by all 

                    relevant disciplines and structured to allow for 

                    change.  The adherence to a method of design 

                    that allows the history of the design and the 

                    instructions for its creation to be included and 

                    referenced for both progress and necessary 

                    changes is very powerful.  Like the sequence 

                    of amino acids in the protein that are derived 

                    from the genes, Figure 89, the primary data 

                    structure of the specifi c architectural design 

                    fi le should exist as an entity within the digital 

                    program in that the code based instructions         86.  Diagram of relationship between genotype and phe-

                    should specify all of the necessary information     notype.  The genes (1-5) on the left govern the forma-

                                                                        tion of a gene product (1 gene - 1 polypeptide).  A gene 

                    required to generate the desired components         product can affect a number of features.  A phenotype 

                    and model.  In this case the transaction code       may be the result of the combined effects of several 

                                                                        gene products.

                    within GC represents an ordered arrange-

                    ment of the instructions necessary for pro-

                    gression of the design.  See Figure 90.

                    GC contains within it a number of paramet-

                    ric instructional commands that defi ne the 

                    shape of the structural elements and the fi nal 

                    form of the structure itself.  A symbolic view 

                    of the transaction script graphically illustrates 

                    the dependencies that each design feature has 

                    with regard to itself and its surrounding mem-

                    bers.  All of the subsequent physical genera-

                    tion of manufactured pieces and the fi nal form 

                    itself are dependent upon the arrangement 

                    and instructions given within the transaction 

                    script.

                                                                        87.  GenerativeComponents Point component and the 

                                                                        subset of update methods by which the Point is recal-

                                                                        culated.

                                                                    85

## [p. 108]

Secondary Structure – The orderly hydrogen 

                                                                                                  bonded arrangements, alpha helix and pleated 

                                                                                                  sheet, if present are called the secondary 

                                                                                                  structure of the protein.  The formation of the 

                                                                                                  secondary structure is a function of the type 

                                   88.  Primary protein structure.  The amino acid chain is       of bonding that occurs within the molecule.  

                                   a long sequence of amino acids.                                See Figure 91.

                                                                                                  Secondary Structure in Practice – In all man-

                                                                                                  ufacturing processes that are completed on a 

                                                                                                  large scale where constructions derived from 

                                                                                                  one piece of material are impossible it is nec-

                                                                                                  essary to rely on the accretion of building ele-

                                                                                                  ments to complete the whole.  Often times 

                                                                                                  these members require a number of opera-

                                                                                                  tions to be performed on them to allow for 

                                                                                                  joining to other members as well as to derive 

                                                                                                  their fi nal form.  CNC manufacturing relies on 

                                                                                                  the output code from the design software to 

                                                                                                  drive the relevant tooling and machines that 

                                                                                                  create the physical elements.  More than a 

                                                                                                  graphical representation of the individual con-

                                                                                                  struction elements the secondary structure of 

                                                                                                  the design holds within it the instructions nec-

                                                                                                  essary for their manufacturing.  This information 

                                                                                                  may appear in the form of code necessary for 

                                                                                                  physical development of the element including 

                                                                                                  laser cutting, milling, roll forming, thermoform-

                                                                                                  ing, brake forming or as information related to 

                                                                                                  the placement of the member either by laser 

                                                                                                  etching or bar code printouts for part scan-

                                                                                                  ning on site.  The secondary structure then is 

                                                                                                  a progression of the primary structure in that 

                                                                                                  the developed code and instructions have 

                                                                                                  been translated from GC language to a vari-

                                   89.  Universal Genetic Code specifying relationship            ety of different languages that can then help 

                                   between the nucleotide bases and the amino acids 

                                   derived from them.  The information contained in the           to defi ne the tertiary form and placement of 

                                   nucleotide sequence of the mRNA is read as three               individual elements. 

                                   letter words (triplets), called codons.  Each word stands 

                                   for one amino acid. 

                                                                                              86

## [p. 109]

Tertiary Structure – The complete three 

                 dimensional conformation of the molecule.  

                 The secondary structure is a local structure 

                 that is formed of and may include the alpha 

                 helical, pleated sheet or random coil structure.  

                 The tertiary structure includes all the second-

                 ary structure and all the kinks and folds in 

                 between.  See Figure 92.

                 Tertiary Structure in Practice – The result 

                 of the transaction script and operations per-

                 formed in the secondary structure produces 

                 the fi nal component form.  This physical man-

                 ifestation of the modeling component rep-

                 resents a single building element that will be 

                 used for fi nal construction.  The component, in 

                 its tertiary form, may function as an indepen-

                 dent building unit or it may be combined with 

                 other elements into a more complex assem-    90. GenerativeComponents transaction fi le.

                 bly.

                 As there is often a need to produce physical 

                 models for verifi cation purposes, GC allows a 

                 user to defi ne features for the scaling of the 

                 model in the primary and secondary struc-

                 tures that enables the output of the tertiary 

                 components to vary from model to full pro-

                 duction size.  The ability of GC to suppress var-

                 ious transaction steps allows the designer to 

                 selectively add or remove detail to the model 

                 depending on the scale to which is it being 

                 produced.  Ideally the elements produced in 

                 this phase will be designed according to their 

                 function either on their own or in concert 

                 with other elements.  

                                                              91. Secondary structure of protein molecule.

                                                           87

## [p. 110]

Quaternary Structure – Refers to the asso-

                                                                                              ciation of two or more peptide chains in the 

                                                                                              complete proteins.  Essentially it is the build-

                                                                                              ing of the active protein molecule through the 

                                                                                              interaction of the unique tertiary forms of the 

                                                                                              peptide chains.  See Figure 93.  Not all pro-

                                                                                              teins exhibit quaternary structure however, 

                                                                                              and they may in fact be fully functional in their 

                                                                                              tertiary conformation. 

                                                                                              Quaternary Structure in Practice – The qua-

                                                                                              ternary structure represents the fi nal assem-

                                                                                              blage of the unique tertiary components.  It 

                                                                                              can be viewed as the functional equivalent 

                                                                                              of an accretion of building elements where 

                                                                                              a larger component is derived from multiple 

                                                                                              smaller or less complex elements.  The depth 

                                                                                              of functional interaction here can occur on 

                                                                                              degrees of involvement with each other.  An 

                                                                                              individual element such as a structural mem-

                                                                                              ber can combine with other members to pro-

                                                                                              duce an elaborate wall structure.  Each ter-

                                                                                              tiary element combines to form a structural 

                                                                                              unit that functions on a large scale.  Alterna-

                                 92.  G-Code for milling machine operation.  The coding       tively, the quaternary structure could also rep-

                                 specifi es a number of different operations or require-      resent an arrayed surface population of adap-

                                 ments that the machine is required to perform.  For 

                                 example:                                                     tive cladding panels for that same wall.  The 

                                 G53 = motion in machine coordiante system                    addition of all the tertiary and quaternary ele-

                                 M01 = optional program stop                                  ments will form the following proteome.  See 

                                 M06 = tool change

                                 G54 = use preset work coordinate system 1                    Figures 94-96.

                                 M3 = turn spindle clockwise

                                                                                              Proteome

                                                                                              The fi nal form of the building and its com-

                                                                                              ponents as realized in its built confi guration 

                                                                                              represents a static version of the proteome 

                                                                                              as captured after all of the relevant design 

                                                                                          88

## [p. 111]

forces have affected it.  The digital version of 

                     the proteome is however able to change and 

                     could have the capacity to drive the evolu-

                     tion of another project with similar formalistic 

                     requirements but varying morphological con-

                     straints.  In essence, a new environmental con-

                     dition will be able to interact with the pro-

                     gram and defi ne a new building with existing 

                     instructions.

                     6.1.6    Interoperability and BIM (Build-

                              ing Information Modeling)

                     In creating a design system that effectively 

                     functions on and within a number of levels to 

                     provide ease of use in all design disciplines, the 

                     issue of interoperability arises.  Interoperabil-

                     ity is a term that refers to the “ability to man-    93.  Tertiary structure of protein molecule.

                     age and communicate electronic and project 

                     data between collaborating fi rms’ and within 

                     individual companies’ design, construction, 

                     maintenance, and business process systems… 

                     Interoperability relates to both the exchange 

                     and management of electronic information, 

                     where individuals and systems would be able 

                     to identify and access information seamlessly, 

                     as well as comprehend and integrate informa-

                     tion across multiple systems.” (Gallaher 2004, 

                     p.ES-1)

                     A number of manufacturing sectors includ-

                     ing computer, automobile and aircraft have 

                     already made advances in the integration of 

                     design and manufacturing, maximizing auto-

                     mation technology, and replacing many paper 

                     documents with electronic equivalents.  The 

                     AEC industry however, has yet to realize the         94.  Quaternary structure of protein molecule.

                                                                       89

## [p. 112]

potential savings available with a widespread 

                                                                                                  application of these approaches.  

                                                                                                  The values quantifi ed for the U.S. capital facili-

                                                                                                  ties supply chain in 2002 indicate that the costs 

                                                                                                  of inadequate interoperability through the 

                                                                                                  life-cycle of a building for the AEC commu-

                                                                                                  nity including specialty fabricators and suppli-

                                                                                                  ers totaled US$5.176 Billion.  This represents 

                                                                                                  between one and two percent of industry rev-

                                                                                                  enue but these values have been recognized 

                                                                                                  as representing only a portion of measurable 

                                                                                                  interoperability cost losses. (Gallaher 2004, 

                                                                                                  p.ES-7)  It is possible to see then how a refor-

                                                                                                  mation in the process and product of design 

                                                                                                  and construction could lead to potential sav-

                                                                                                  ings with regard to both time and money.

                                   95.  Structural elements.                                      BIM as it is known is a term that describes a 

                                                                                                  number of modeling environments that allow 

                                                                                                  for the partial parametric generation of a 3D 

                                                                                                  building model with associated logical out-

                                                                                                  put of 2D drawings, component lists, building 

                                                                                                  costs, structural analysis, etc.  On top of this is 

                                                                                                  the ability for information exchange between 

                                                                                                  participants in all aspects of the building from 

                                                                                                  design to manufacture to construction.  While 

                                                                                                  other industries using integrated digital envi-

                                                                                                  ronments such as CATIA, SolidWorks, etc. have 

                                                                                                  attempted to utilize a holistic design approach

## [p. 113]

6.1.7    Additional Areas for Further                is the programmer that defi nes the amount of 

                             Research                                    user input that will allow progression to occur.  

                                                                         While a GA may carry out all of its computa-

                    There are a number of additional areas that          tion automatically, an Interactive Genetic Algo-

                    are well suited to and contribute to the pro-        rithm may be used that requires human inter-

                    gressive development of digital design for the       vention at a number of key steps that have 

                    AEC community.  These approaches also strive         been defi ned for it.  

                    to develop a design through a minimal amount 

                    of instructions and design parameters.  The fol-     The GA is essentially a structured method of 

                    lowing section briefl y outlines the premise of      selecting between alternative design possi-

                    each but they are intended for illustrative pur-     bilities.  In principle, this method of selection 

                    poses and as such lie outside the scope of this      could be integrated into the GC design envi-

                    thesis.                                              ronment to aid in the selection or derivation 

                                                                         of designs that must fulfi ll a number of quanti-

                    6.1.7.1 Genetic Algorithms                           fi able criteria.

                    In a Genetic Algorithm (GA), a chromosome            6.1.7.2 Rule Based Programming

                    (also sometimes called a genome) is a set of 

                    parameters which defi ne a proposed solution         The fundamental approach to rule based pro-

                    to the problem that the GA is trying to solve.       gramming is the implementation of replace-

                    The chromosome is often represented as a             ment rules for processing rather than proce-

                    simple data string although a wide variety of        dural constructs.  In this approach a number 

                    other data structures are also in use as chro-       or collection of rules is developed that defi nes 

                    mosomes.                                             the actions that are to be taken by the program 

                                                                         with regard to specifi c situations.  In an archi-

                    A GA creates many chromosomes, either ran-           tectural sense the design requirement may be 

                    domly or by design, as an initial population.        the effective storage of the design experience 

                    These chromosomes are each evaluated by              from various projects, not at the level of the 

                    the fi tness function, which ranks them accord-      design itself, but at the level of the principle 

                    ing to how good their solution is. The chro-         of assembly behind the designs.  Rather than 

                    mosomes which produced the best solutions,           actually documenting the design itself the pro-

                    relatively speaking within the population, are       gram is infused with the rules for the design 

                    allowed to breed, also called crossover. The         and it creates the required details depend-

                    best chromosomes’ data is mixed, hopefully           ing on the particular stylistic or construction 

                    producing more refi ned subsequent genera-           principles that are written into the program. 

                    tions.  The functional design of the GA can          (Seebohm 1998)  Here, the program is act-

                    vary dramatically from one to the next and it        ing in a manner that allows for multiple out-

                                                                     91

## [p. 114]

comes depending on the current environment 

           in which it is functioning.  The possibilities for 

           a functional and automatic feedback loop exist 

           but there is added complexity in tracing the 

           logic string and ensuring quality assurance.

           6.1.7.3 Nanotechnology

           Nanotechnology represents the physical real-

           ization of AEC industry on a truly cellular level.  

           By reducing architectural constructions to a 

           scale measured in nanometers the possibilities 

           for organic or quasi-organic forms become 

           possible.  A building could theoretically be pro-

           grammed to grow itself based on the instruc-

           tions of the architect.  Like current 3D print-

           ing technology the building could raise itself as 

           one cohesive unit rather than an amalgama-

           tion of disjunctive assemblies.  Buildings could 

           repair themselves, transmit information about 

           their current status with regard to tempera-

           ture, stress, fatigue, air quality and any number 

           of other desirables.  They could change shape, 

           porosity with regard to ventilation or ingress/

           egress.  The possibilities at this level of archi-

           tectural construction are almost limitless but 

           the fruition of development in this area will 

           only come with an incredible design mecha-

           nism that is able to control it.

                              92

## [p. 115]

6.2     Design Concept #2 - Ruled 

                           Surface Structure

                   The complexity involved in creating non-

                   orthogonal structures is often associated with 

                   higher design, production and labor costs.  This 

                   has been a negative infl uence on the prolifera-

                   tion of these types of structures particularly 

                   in North America, where the economic vision 

                   focuses on the short term.  This design inves-

                   tigation seeks to develop a concept for the 

                   design and construction of these types that 

                   satisfi es the criteria outlined in Section 5.3.  

                   6.2.1 Inspiration

                   The development of an organism from youth 

                   to maturity occurs with a number of environ-

                   mental and internal stresses acting on it which 

                   help to determine its fi nal form.  As illustrated 

                   previously however, their response to these 

                   stresses may act in a static or dynamic way.  

                   Bone morphology changes throughout time 

                   and is in a constant state of reformation to bal-

                   ance the forces acting on it.  This closed loop 

                   system of reformation is able to sense a vari-

                   ety of environmental variables and change itself 

                   accordingly.  In addition to the dynamic nature 

                   of bone, it also possesses a unique cross-

                   linked internal structural pattern that provides 

                   incredible strength with a minimal investment 

                   of material and weight.  The structure of the 

                   tibia bone in the human leg is capped by a 

                   widened tip that covers the hollow cylindrical 

                   shaft that it rests on.  The interesting structural 

                   implication here is how the vertical pressures  97.  Head of the human femur in section

                                                                   98.  Crane-head and femur

                   acting upon the head of the bone are trans-     99.  Diagram of stress-lines in the human foot.

                                                                93

## [p. 116]

ferred to the walls of the hollow shaft below.  

                                                                                                Within the hollow space there exists a variety 

                                                                                                of living tissue including marrow, blood vessels, 

                                                                                                and others; among which is an intricate lattice-

                                                                                                work of “trabeculae” of bone which form the 

                                                                                                “cancellous tissue.”   See Figure 97.

                                                                                                “The trabeculae, as seen in the longitudinal 

                                                                                                section of the femur, spread in beautiful curv-

                                                                                                ing lines from the head to the hollow shaft of 

                                  100.  Dragonfl y wing.                                        the bone…nothing more nor less than a dia-

                                                                                                gram of the lines of stress, or directions of ten-

                                                                                                sion and compression, in the loaded structure:  

                                                                                                In short, that Nature was strengthening the 

                                                                                                bone in precisely the manner and direction in 

                                                                                                which strength was required…”  (Thompson 

                                                                                                1963, p976)  See Figures 98-99.

                                                                                                The dragonfl y wing appears to exhibit a com-

                                                                                                plicated and seemingly random structural sys-

                                                                                                tem consisting of a network of various sized 

                                                                                                veins.  See Figure 100.   To duplicate and enlarge 

                                                                                                this structure in order to fulfi ll an architectural 

                                                                                                role would be impractical and extremely labor 

                                                                                                intensive. However, if the wing is examined in 

                                  101.  Primary and secondary veins of dragonfl y wing.         fi ner detail it is possible to identify the over-

                                                                                                all structural trends that determine its primary 

                                                                                                confi guration and thus design a simpler archi-

                                                                                                tectural structure with similar properties.  The 

                                                                                                wing is traversed longitudinally by a series of 

                                                                                                strong veins that run more or less parallel to 

                                                                                                each other.  Finer veins run between the main 

                                                                                                veins in a meshwork of “cells.”  See Figure 101.  

                                                                                                The walls of the cells within the meshwork 

                                                                                                while subdivided into a matrix exhibit tenden-

                                                                                                cies to follow lines of running at angles to the 

                                                                                                main structural veins.  (McLendon 2005, p2)

                                                                                            94

## [p. 117]

6.2.2 Design Outline                                  different physical properties for strength, etc.  

                                                                          This situation may exist in a multi-fl oor con-

                    In order to begin development of a design             struction where the members on the lower 

                    approach for non-orthogonal structural build-         fl oors are stronger yet have identical morphol-

                    ing skins that allow for fl uidity, changeability     ogy to members directly above them.  While 

                    and overall ease of design, manufacture and           this may result in an increase in the require-

                    construction it is fi rst necessary to arrive at      ment for construction documentation it does 

                    a proper form for exploration.  A number of           make manufacturing easier as there is a large 

                    surfaces have been investigated in this thesis        degree of replication and standardization.  Lin-

                    from fl at to compound curves.  Of particu-           ear components also reduce the requirement 

                    lar interest is the ruled developable surface in      for intensive CNC manufacturing that although 

                    that curvilinear forms can be derived from            quite effi cient and accurate can become quite 

                    fl at panel materials.  While this characteristic     labor intensive if each element requires a dif-

                    is important with regard to ease of manufac-          ferent setup for clamping, forming, etc.

                    ture and construction of the surface condi-

                    tion it also allows for a novel approach to the       In a curvilinear construction there is often a 

                    development of the structural members that            requirement for many unique pieces that need 

                    form it.  With a conscientious approach to the        to be placed in many different locations and 

                    design of the ruled surface it is hypothesized        transferability cannot occur.  Although it may 

                    that the primary, secondary and tertiary mem-         at fi rst seem daunting to construct a building 

                    bers can all be fabricated out of identical width     enclosure with many unique pieces the simple 

                    linear lengths of material that must merely be        fact that they are unique limits their organiza-

                    bent in one direction if at all depending on          tion to only one possibility.  With an effi cient 

                    their function and location.  This will have to be    numbering or labeling system it is possible to 

                    done however by putting aside some current            construct it with a small number of instructions 

                    assumptions of design and construction which          for assembly rather than a comprehensive col-

                    will be illustrated when required.                    lection of construction drawings for building 

                                                                          element location and orientation.  In effect, the 

                    The shape of a building element has the capac-        instructions for the physical form of the build-

                    ity to be different or identical to any number        ing itself are contained within the three dimen-

                    of other elements within the building.  In a rel-     sional conformation of the individual build-

                    atively simple rectilinear building many of its       ing elements.  The presence of many unique 

                    elements could theoretically be interchanged          non-orthogonal structural members however 

                    as with one wall stud for another.  Without           often requires multiple elaborate template lay-

                    proper and extensive documentation how-               outs for laser or plasma cutting usually carrying 

                    ever it becomes diffi cult to properly locate ele-    with them a certain degree of material waste.

                    ments that may have similar confi gurations but 

                                                                      95

## [p. 118]

As noted in section 2.1.4 Hierarchy of Structure,     manufacture while maintaining morphological 

                              the trend for orthogonal constructions in the         individuality for uncomplicated construction.  

                              dissipation of internal and external forces is to     At the same time the digital portion of the 

                              transmit them downward in an additive verti-          design will facilitate a generative closed feed-

                              cal fashion.  The presence of localized stresses      back loop where additions to the whole or 

                              in the form of impact or environmental anom-          changes to certain predefi ned areas will pro-

                              alies can cause catastrophic failure to occur.        vide automatic update of all the required fab-

                                                                                    rication and construction requirements with a 

                              Structural patterning is quite prevalent in con-      minimal number of instructions.  The in-built 

                              struction today where multiple unitized ele-          customizability of the design will also allow the 

                              ments are distributed throughout the building         design to be useful in a variety of building sce-

                              in an effort to reduce design and construc-           narios rather than be unique to only one site.  

                              tion time.  The case quite often though is that       The physical form of the design will be derived 

                              there is an associated hierarchy of structural        so that stresses are distributed throughout 

                              forces where smaller elements dissipate their         the structure in a number of different direc-

                              forces into successively larger elements in a         tions thus minimizing the presence of localized 

                              vertical fashion until they are transmitted to        stresses and the possibility of structural failure.  

                              the ground.  A failure in one of the base ele-        In the end it is hoped that through an effi cient 

                              ments can prove catastrophic for the build-           and logical process of design, manufacture and 

                              ing as the force distribution is additive in each     construction that it will be possible to pro-

                              subsequent element.  Natural principles favor         duce a fi nal form that is aesthetically pleasing, 

                              an alternative approach to the distribution           applicable and relevant in a variety of building 

                              of forces where they are dissipated among             applications, effi cient for affordable construc-

                              many different pathways thus avoiding local-          tion and structurally sound.  

                              ized stresses on the organism.  In this thesis, 

                              the natural approach to structural design prin-       In keeping with the design model outlined in 

                              ciples as they relate to exoskeletons will be         6.1 Design Documentation there are a number 

                              used.  Structure and skin will be integrated into     of approaches that can be taken to arrive at a 

                              one unit rather than existing as separate enti-       desired fi nal product.  The direction outlined 

                              ties.  The fi nal form of the structural elements     below represents one pathway of the design.  

                              will be partially dependent on the fi nal form of     After the resultant model has been created 

                              the skin which will

## [p. 119]

set out in Section 6.1 the focus of this design 

                   concept will be contained within an approach 

                   to developing a base parametric model that 

                   is suitable for export and use in a variety of 

                   different analysis and manufacturing programs.  

                   GenerativeComponents will be used as the 

                   digital software for generation of the design 

                   and as a platform for drawing and manufactur-

                   ing export.  

                   6.2.3 Design Product

                   The starting point is to develop a design con-     102.  Graph Variables

                   dition that can be applied to a variety of sites 

                   and applications.  Once that scenario is in place 

                   it is possible to begin developing a model that 

                   is able to adapt to those conditions.  To reduce 

                   initial complexity of the design requirements 

                   the façade was restricted to only one face of a 

                   potential building.  This type of condition could 

                   exist in an infi ll condition or within a restrictive 

                   urban site.  

                   1.   Identifi cation of key parameters that will 

                        contribute to the functionality of the 

                        model and allow for the desired level of 

                        variability in the design.

                   When the initial design of a building is tak-

                   ing place there are often a large number of 

                   variables that are unfi xed and changeable.  By 

                   carefully planning the strategy for the develop-

                   ment of the building concept then it becomes 

                   possible for these variables to become exactly 

                   that.  Changes and deformations to the overall 

                   design can be quickly visited and revisited.  In 

                   this case the following variables will be allowed 

                   for.                                               103.  Layout parameters and defi ning curves.

                                                                   97

## [p. 120]

- Wall length

                                                                                        - Wall height

                                                                                        - Wall thickness

                                                                                        -    Number of sections for deriving the pri-

                                                                                             mary structural elements

                                                                                        -    Number of sections for deriving the sec-

                                                                                             ondary/tertiary elements

                                                                                        Now that the variables for design have been 

                                                                                        identifi ed it is possible to begin working in GC 

                                                                                        to create graph variables that defi ne these 

                                                                                        parameters and allow for their manipulation.  

                                                                                        It should be noted however that the expres-

                                                                                        sion deriving the variable output may in fact 

                                                                                        rely on the output from another component 

                                                                                        which must be created before the GV in order 

                                                                                        to be recognized due to the dependency hier-

                               104.  YZ Planes and the resulting BsplineSurface and     archy.  In this case all of the expressions for the 

                               primary structural member layout lines.                  GVs will be independent and stand alone in 

                                                                                        their variability.  See Figure 102.

                                                                                        2.  Development of the design model with 

                                                                                             a logical progression of generative fea-

                                                                                             tures.  

                                                                                        The fi rst step here is to create a virtual enve-

                                                                                        lope of layout parameters that allow for the 

                                                                                        three dimensional defi nition of the fi nal form.  

                                                                                        The value of the layout lines that describe these 

                                                                                        parameters are based on the GVs created 

                                                                                        previously.  Layout points are created along 

                                                                                        a series of equally spaced bays which defi ne 

                                                                                        the upper and lower curves that will defi ne 

                                                                                        the ruled surface.  The position of each layout 

                                                                                        point is individually variable which allows the 

                                                                                        designer to change the defi nition curves and 

                               105.  XZ Planes and the resulting secondary/tertiary     the subsequent surface derived from them.  

                               layout lines derived from the BsplineSurface.            See Figure 103.

                                                                                    98

## [p. 121]

The location of the primary structural ele-

                    ments required for the facade are developed 

                    by intersecting a variable number of evenly 

                    spaced YZ planes based on subdivision of the 

                    Façade_Length with the curves defi ning the 

                    ruled surface.  The points produced from the 

                    intersection of those curves will then be used 

                    to defi ne both the structural members and 

                    the RuledBsplineSurface facade.  This approach 

                    guarantees that the structural members will lie 

                    directly in plane with the ruled surface itself.  

                    When dealing with bezier curves and surfaces 

                    derived from them there can be discrepancy in 

                    correlation between the surface and curves if 

                    there are a different number of nodes present 

                    as is the case here.  The layout lines that must 

                    be physically replicated on site for foundation 

                    work, etc. can be derived from the BsplineSur-

                    face thus maintaining the best possible con-

                    struction tolerance.  See Figure 104.              106.  Extrusion of the primary and secondary/tertiary 

                                                                       members in the Y direction.

                    A variable set of XZ planes is created that run 

                    perpendicular to the YZ planes.  The intersec-

                    tion of these with the BsplineSurface will pro-

                    duce curves defi ning the conformation of the 

                    secondary/tertiary structural members.  In 

                    defi ning the members this way it is intended 

                    that their natural conformation will follow lines 

                    of stress within the structure where member 

                    density will increase based on the curvature 

                    of the facade.  It should be noted that in this    107.  Direction of translation and associated decrease in 

                                                                       wall thickness.

                    model, the derivation of the members occurs 

                    without any external loading conditions which 

                    would need to be addressed in subsequent 

                    iterations.  The fact that secondary/tertiary 

                    members meet the primary structural mem-

                    bers at varying angles develops a triangulated 

                                                                    99

## [p. 122]

structural framework that resists not only ver-

                                                                                             tical compression but horizontal shear in both 

                                                                                             the X and Y directions.  The other appreciable 

                                                                                             benefi t to secondary/tertiary members being 

                                                                                             derived this way comes from the fact that they 

                                                                                             are curvilinear in the direction perpendicular 

                                                                                             to, and linear in line with, their length.  This 

                                                                                             means that their fabrication can sidestep the 

                                                                                             CNC driven cutting that would be required 

                                                                                             if they were curved in the direction of their 

                                                                                             length.  It should be noted that this arrange-

                                                                                             ment can only be realized with the use of a 

                                                                                             developable ruled surface.  See Figure 105.

                                                                                             After construction of the curves defi ning the 

                                                                                             primary and secondary/tertiary members 

                                                                                             they can be extruded in the Y direction the 

                                 108.  UV Points on BsplineSurface                           desired depth of the wall.  A variable length 

                                                                                             line whose expression is defi ned by the Wall_

                                                                                             Depth GC is used to create extruded Bspline-

                                                                                             Surfaces along the structural layout curves.  

                                                                                             This method of extrusion creates structural 

                                                                                             members that are all of an identical depth.  

                                                                                             See Figure 106.  Once again this aids in ease of 

                                                                                             production by the allowing the manufacturer 

                                                                                             to create the members out of linear strips of 

                                                                                             plate steel that can be easily sheared or cut to 

                                                                                             width with minimal adjustment of machinery.  

                                                                                             While this does allow for ease of production 

                                                                                             there are some considerations that must be 

                                                                                             recognized in order to prevent design over-

                                                                                             sights from occurring.  The straightforward 

                                                                                             extrusion or translation of a surface, as is the 

                                                                                             case here, into a solid produces one in which 

                                                                                             the wall thickness will vary depending on the 

                                                                                             curvature of the surface and its alignment to 

                                 109.  Surface panels on BsplineSurface                      the direction of translation.  See Figure 107.  As 

                                                                                        100

## [p. 123]

surface curvatures increase and the wall direc-

                         tion comes closer to the direction of transla-

                         tion, the wall thicknesses will diminish until a 

                         point is reached were the two surfaces would 

                         intersect.  If the planar constraints allow for 

                         an extruded surface without intersection then 

                         the inner and outer surfaces will be identical 

                         in shape.  This means that any panel confi gu-

                         rations derived from the surfaces will also be 

                         identical inside and out effectively halving the 

                         number of unique panel confi gurations that 

                         would be necessary with a surface that has 

                         been offset.  If intersections or unacceptable 

                         wall depths occur then either an adjustment 

                         of the layout curves defi ning the surface or a 

                         different design approach would be required 

                         at that location.

                                                                                         110.  Point grid created based on location of the 

                         3.   Creating output conditions for visualiza-                  primary elements

                              tion, construction drawings, fabrication 

                              etc.

                         Now that the design model has been created 

                         it is necessary to begin the process of translat-

                         ing the developmental and visual information 

                         it contains into a format for manufacturing and 

                         construction.  While the BsplineSurface defi n-

                         ing the skin condition could potentially be con-

                         structed from one large piece of material, this 

                         obviously becomes diffi cult when the struc-

                         ture increases in size.  With this being the case 

                         it becomes necessary then to subdivide the 

                         surface into a number of smaller surface pan-

                         els for manufacturing and construction.  

                         There are a multitude of ways to create the                     111.  Surface panels created from projection of point 

                         surface panels with each approach having dis-                   grid onto the BsplineSurface

                                                                                    101

## [p. 124]

tinct benefi ts and drawbacks.  Here, two of 

                                                                                                those approaches will be developed.  The fi rst 

                                                                                                method involves populating the BsplineSur-

                                                                                                face with a series of variable UV points which 

                                                                                                are points described on a 3D surface by 2D 

                                                                                                transformations along it.  These points serve 

                                                                                                to defi ne the corners of the surface panels 

                                                                                                which can then be derived by creating shapes 

                                                                                                between them.  See Figure 108-109.

                                                                                                The shapes created between the UV points are 

                                                                                                planar and as a result do not conform exactly 

                                                                                                to the ruled surface.  This condition can result 

                                                                                                in improper sizing of the manufactured panels.  

                                                                                                As the density of UV points on the surface is 

                                                                                                increased so too does the correlation of their 

                                                                                                form to the native form of the BsplineSurface 

                                  112.  ConstructionDisplay is added with text for loca-        thus reducing error.  The position of the UV 

                                  tion of the panels on the facade.                             points does not correspond with the location 

                                                                                                of the primary structural members so a sepa-

                                                                                                rate panel attachment system would need to 

                                                                                                be developed which would increase produc-

                                                                                                tion and construction cost.  In this particular 

                                                                                                design scenario this method of surface subdivi-

                                                                                                sion is the least effi cient.

                                                                                                The second method involves creating a virtual 

                                                                                                point grid corresponding to the location of the 

                                                                                                primary structural members in the X direction 

                                                                                                and an arbitrary value set by the designer in 

                                                                                                the Z direction.  The panels produced here are 

                                                                                                similar to the UV derived panels in that they 

                                                                                                are composed of planar surfaces and hence 

                                                                                                are not as accurate as possible.  Their fastening 

                                                                                                to the structure becomes much easier in that 

                                  113.  Detail of ConstructionDisplay and text style ap-        their vertical edges line up with the primary 

                                  plied to the panels for export to FabricationPlanning.        structural members.  See Figure 110-111.

                                                                                           102

## [p. 125]

The third method would build on the sec-

                   ond in that a point grid would again be used 

                   to defi ne panel corner points on the surface.  

                   This time however, and with further research, 

                   the panels would be derived by intersecting 

                   the lines connecting the surface points with 

                   the BsplineSurface and fl attening them.  This 

                   would create panels that are developed from 

                   the BsplineSurface itself thus being much more 

                   accurate than the planar approximations from 

                   the fi rst and second methods.  

                   The fourth method of panel development 

                   would involve extracting and developing the 

                   entire BsplineSurface into a separate fabrica-

                   tion fi le where it could be subdivided with a 

                   regular grid.  The interior panels in this instance 

                   could all me made exactly the same size which     114.  Flattened panels ready for laser cutting in the 

                                                                     FabricationPlanning fi le.

                   would greatly reduce manufacturing time.  

                   However, the same situation for fastening 

                   would arise as with the fi rst method.

                   The benefi t of using GC to develop these 

                   methods is that each one can exist within the 

                   same transaction fi le and they can be selec-

                   tively turned on or off when required.  This 

                   allows for the designer to revisit, change or 

                   develop any one or combination depending 

                   on any number of construction variables or 

                   requirements such as cost, delivery schedules, 

                   manufacturing capabilities, etc.

                   After the panels have been created in the 3D 

                   model it is possible to export them to another 

                   fi le for fabrication.  A new Model is created 

                   that is used to import the fl attened panels      115.  Detail of text style applied to panels for ease of 

                   from the 3D model.  A TextStyle is created        identifi cation and optional scribing by laser. cutter

                                                                 103

## [p. 126]

that will be used to label the individual panels     Advantages

                             for laser etching and their location in the 3D 

                             model.  The FabricationPlanning feature is used      Translating the BsplineSurface instead of off-

                             to export the 3D panels into the 2D Model            setting it.

                             and the TextStyle is applied.  The visibility of 

                             the TextStyle is controlled by creating a feature    -   Allows the inner and outer panels to be of 

                             called ConstructionDisplay that can toggle it            identical shape.

                             on or off.  The 2D FabricationPlanning  fi le can    -  Allows the structural members to be 

                             then be directly exported to a laser cutter for          composed of identical width material.

                             fabrication.

                                                                                  Vertically sectioning the BsplineSurface to 

                             The development of all of the structural mem-        derive the secondary/tertiary members.

                             bers in the model and for fabrication and con-

                             struction would proceed in a similar manner.         -   Members can be made from linear strips 

                             As of the writing of this thesis the GC pro-             of roll formed fl at sheet.

                             gram is still in its pre-beta phase and as such      -   Laser/plasma cutting is required only at 

                             does not contain all of the functionality that is        structural intersections and not at struc-

                             expected with the fi rst release.  The ability to        tural member edges.  Exterior edges can 

                             develop and export G-code required to drive              be sheared which drastically reduces man-

                             CNC rollers and manufacturing machines is                ufacturing time.

                             expected to be contained with the fully devel-       -   The 3D conformation of the members 

                             oped version.                                            ensures that they can only be placed in 

                                                                                      their correct location.

                             6.2.4 Design Evaluation

                                                                                  Development of the model in the GC para-

                             The design concept developed here represents         metric environment.

                             an approach to design that uses biomimetic 

                             principles of stress based growth, self assem-       -   The relative freedom of hierarchical orga-

                             bly, sensing and responding, scale increases, and        nization created in the transaction fi le 

                             the power of shape.                                      allows a completed and sometimes awk-

                                                                                      wardly built model to be easily updated 

                             The benefi ts derived from using these princi-           and the feature elements to be laid out 

                             ples in the GC parametric design environment             in a cleaner more concise manner.  Any 

                             are appreciable with regard to both the design           new person coming into the project will 

                             itself as well as the associated manufacturing           know and be able to follow in a linear 

                             and production requirements.                             manner exactly how the model was built, 

                                                                                      what its outputs are and the method in 

                                                                             104

## [p. 127]

which it can be manipulated in an existing    -    The digital model is relevant only with a 

                        or potential context.  See Figures 116 &           design brief that would benefi t from its 

                        177.                                               use.  A different type of design approach or 

                    -   Variability of the design allows for an anal-      morphological requirement would neces-

                        ysis of structure and rapid readjustment of        sitate the development of a new model.

                        the design to suit.

                    -   Dimensional material changes due to scale 

                        increases can be factored into the model.

                    -   Drawings and code required for manu-

                        facturing and production are instantly 

                        updated as required.

                    -   Multiple design scenarios can be visited 

                        and revisited without loss of functionality 

                        or invested time.

                    -   The completed model can be used for a 

                        variety of projects due to its adaptability.

                    Disadvantages

                    -  As the curvature of the layout curves 

                        increase the effective thickness of the dis-

                        placed surface becomes less.  If the cur-

                        vature becomes too great then the thick-

                        ness will be insuffi cient to allow for the 

                        necessary building components and insu-

                        lation.  In this case it would be necessary 

                        to incorporate a new wall component 

                        that replicates the function of the original 

                        wall component in its own implementa-

                        tion.  While the façade will then develop 

                        a characteristic crease in its folding the 

                        material and fi nancial benefi ts of the over-

                        all design will still be maintained.  The 

                        incorporation of the new component will 

                        essentially change the direction of extru-

                        sion in a direction perpendicular to the 

                        facade direction.

                                                                  105

## [p. 128]

116.  Instantaneous translation of building confi guration

                                     117.  Instantaneous translation of building confi guration

                                    106

## [p. 129]

118.  Rendering of potential building confi guration.

                                107

## [p. 130]

6.3       Design Concept #3 - Folded 

                                                                                                         chevron structure

                                                                                               Structure in nature takes many forms which 

                                                                                               serve to absorb the stresses and environmen-

                                                                                               tal conditions imposed on an organism.  Of 

                                                                                               particular interest with regard to this design 

                                                                                               concept is that of folded and deployable struc-

                                                                                               tural forms.  This section will examine both 

                                                                                               static and dynamic deployment with the devel-

                                                                                               opment of a design for each.

                                                                                               6.3.1 Inspiration

                                                                                               As a variety of natural organisms develop they 

                                                                                               undergo deployment as a process of attaining 

                                                                                               their fi nal form.  A tightly packaged and folded 

                                                                                               parcel will unfold according to predetermined 

                                                                                               patterns that determine its fi nal shape.  This 

                                                                                               process occurs in insect wings, fl ower petals 

                                                                                               and plant leaves.  Insect wings are an interest-

                                                                                               ing structural group in that different insects 

                                                                                               display various methods of deployment.  The 

                                                                                               dragonfl y wing is deployed by fi lling its primary 

                                                                                               structural veins with hemolymph which also 

                                                                                               serves to prevent it from becoming brittle.  

                                                                                               The wing itself however maintains its shape 

                                                                                               once deployed and it is its passive bending that 

                                                                                               allows for the dragonfl y’s unique capabilities of 

                                                                                               fl ight.  (McLendon 2005, p1)

                                                                                               A beetle on the other hand must employ a 

                                  119.  Right hind wing of Priacma Serrata (bleach beetle)     system for repeated wing deployability as the 

                                  showing folding pattern and the major veins (RA & MP).       larger and fragile hind wings must fold in order 

                                  120.   Digitized folding pattern of Cantharis Livida.        to be protected by their more robust fore-

                                  121.  Basic mechanism of four panels connected by four 

                                  folding lines that intersect at one point.  Most complex     wings.  The patterns of folding as seen in Fig-

                                  folding patterns consist of a combination of several basic 

                                  mechanisms.                                                  ures 119-121, to exhibit rules for folding that 

                                                                                          108

## [p. 131]

have been described in mathematical terms.  

                   (Haas 1998, p2-6)

                   The pattern of unfolding in the beetle wing 

                   is similar to that of the hornbeam leaf which 

                   has been examined by Julian Vincent, co-direc-

                   tor of the department of biomimetics at Uni-

                   versity of Reading.  The similarities of folding 

                   structures here also parallel the developments 

                   of Koryo Miura, a Japanese space scientist, in 

                   the fi eld of origami.  In 1970, Miura proposed 

                   a paper folding pattern – named Miura-ori – 

                   that folds up in two dimensions at right angles 

                   thus taking up very little space.  Its deployment 

                   is also unique in that it unfolds by pulling only 

                   on the two ends without subsequent hand 

                   repositioning.  (Forbes 2000).  See Figures 122 

                   & 123.

                   Until recently the Muira-ori technique was dif-

                   fi cult to implement on large sheet structures 

                   that require a multitude of folds.  Research 

                   Professors at Rutgers University however, 

                   developed a technique to produce a prod-

                   uct similar to the Miura-ori folds through roll 

                   formers.  The product of their research was 

                   subjected to stress analysis against conven-

                   tional honeycomb structures and was found 

                   to surpass them in all regards. (Basily 2004a).  

                   See Figures 124 & 125.

                   6.3.2 Design Outline

                   The issue of deployability in nature is an inter-

                   esting one due to the relevance it has in both     122.  Miura-ori pattern & Hornbeam leaf blooming.

                   architectural design and construction.  The pro-   123.  Folded sheet with Miura-ori pattern.

                                                                      124.  Continuous sheet folding machine.

                   cess of deployability in an architectural sense    125.  Continuous sheet folding machine.

                                                                  109

## [p. 132]

can occur in either a static or dynamic way.         physical manifestation.  The structure develops 

                              The two designs developed here, while similar        through a series of iterative processes that 

                              with regard to the base chevron shape that           produce a fi nal form.  The manufacturing and 

                              they use, are meant as separate explorations         construction of the design occurs in a number 

                              into the applicability of parametric design in       of stages with the structure essentially grow-

                              the context of deployability.  The static deploy-    ing in place.  This deployment of built form can 

                              ment design seeks to derive instantly update-        thus be thought of not only in a physical sense 

                              able instructional information for laser cut-        but also in a temporal sense.  The reference 

                              ting and brake-forming operations that will          to static deployment here represents a pro-

                              yield the proper three dimensional forms.  The       cess that results in the generation of a static 

                              dynamic deployment design will see the cre-          form derived from the deployment of individ-

                              ation of a system that will allow an individual      ual constituent parts, in this case plate folded 

                              chevron component to be arrayed and manip-           structural members, into a compound curved 

                              ulated in real time for ease of manufacturing        surface.  The form will be created from linear 

                              with regard to itself as well as the required        strips of fl at plate steel that are cut and folded 

                              structures on which it will depend for their         into the correct orientation.  Like the fl exible 

                              deployment.                                          structure of the wing before being stiffened 

                              These two systems then, represent differ-            the native form of the fl at plate steel exhibits 

                              ent approaches to nature’s process of sens-          a low resistance to bending which is increased 

                              ing and responding.  In the fi rst case the chev-    through mechanical folding into a modifi ed 

                              ron pattern will sense (receive input) from          Miura-ori pattern.  In this case the typically 

                              the form of the surface to which it is applied       planar chevron will be required to exhibit a 

                              and it will respond (create output) for the          slight deformation in one dimension which can 

                              necessary information related to its manufac-        be kept small enough to be attained through 

                              ture.  The second design will be a preliminary       slight tension induced in construction rather 

                              platform that serves to act as inputs for the        than with mechanical bending in their manu-

                              development of additional design products            facture.

                              (outputs).  These additional products could 

                              represent folded and unfolded layout dimen-          GenerativeComponents will be used to 

                              sions and coverage areas, deployability paths        develop the compound surface and the fl at-

                              for the design of collapsible linkages, or volume    tened strips for manufacturing.  The surface 

                              requirements for storage.                            confi guration will be responsive to user input 

                                                                                   and the Miura-ori pattern derived from it will 

                              Static Deployment                                    compensate to suit any desired curved sur-

                                                                                   face.

                              Architecture as it relates to built form does 

                              not arise spontaneously either in its design or 

                                                                               110

## [p. 133]

_(página sin capa de texto)_

## [p. 134]

The BsplineSurface is then populated with a 

                                                                                                          grid of UV points.  See Figure 128.  The degree 

                                                                                                          to which the surface is divided and populated 

                                                                                                          by the points is dependent on the U_Variable 

                                                                                                          and V_Variable graph variables.  An identical 

                                                                                                          confi guration of UV points is offset from the 

                                                                                                          surface UVs in order to establish a point fi eld 

                                                                                                          in which the chevrons can be created.  See Fig-

                                                                                                          ure 129.  The height of the offset points above 

                                                                                                          the BsplineSurface is dependent on the Offset 

                                     126.  Graph Variables.                                               graph variable. 

                                                                                                          The development of the chevrons is a four 

                                                                                                          part process in that each facet of an individual 

                                                                                                          chevron unit is programmed independently.  

                                                                                                          Each transaction however, creates one facet of 

                                                                                                          every chevron on the surface.  See Figure 130.  

                                                                                                          In this way, the whole surface is populated with 

                                                                                                          only four individual steps.  See Figure 131.  The 

                                                                                                          facets that are created automatically confi gure 

                                                                                                          themselves to suit the localized morphologi-

                                     127.  Initial BsplineSurface.                                        cal conditions of the surface to which they are 

                                                                                                          applied.  

                                                                                                          Once the chevron facets have been devel-

                                                                                                          oped and tested for functionality and variabil-

                                                                                                          ity it is then possible to convert the system 

                                                                                                          into a new Generative Component Feature 

                                                                                                          that can be used and applied to future designs 

                                                                                                          much like the use of a Point, Line or Surface.  

                                                                                                          The Generate New Feature Type dialog box 

                                                                                                          allows one to create a name for the new fea-

                                                                                                          ture as well as defi ne the input and output 

                                                                                                          parameters that the new feature will use for 

                                                                                                          its creation.  In this case, the BsplineSurface will 

                                                                                                          be used as the input for the development of 

                                     128.  UV Points on BsplineSurface.                                   the chevrons.  The user will be prompted to 

                                                                                                    112

## [p. 135]

defi ne values for the Offset, U_Variable and 

         V_Variable.  These values may be changed at 

         any time.  See Figure 132.

         After creating the new feature it can be 

         applied to any BsplineSurface that the user 

         wishes.  Here, the feature has been applied to 

         the ruled surface that was created in Design 

         Concept #2.  As noted, countless morphologi-

         cal possibilities exist from this single derived 

         feature.  See Figure 133, 134 & 135.

                                 129.  Offset points from UV points.

                                 130.  Chevron facet development

                                113

## [p. 136]

131.  Full chevron facet surface.

                                                                                               133.  Application of chevron component to Design 

                                  132.  Generate Feature Type Interface.                       Concept #2

                                                                                          114

## [p. 137]

134.  Sequence of renderings showing facade reconfi gu-

         ration and instantaneous chevron component update.

                                115

## [p. 138]

135.  Sequence of renderings showing canopy reconfi g-

             uration and instantaneous chevron component update.

                                    116

## [p. 139]

Dynamic Deployment

                     This exercise investigates the associative 

                     aspect of GC with regard to dynamic control.  

                     While relatively straightforward in morphol-

                     ogy, the development of the chevron in this 

                     case is based not on the form of the surface to 

                     which it is applied, rather its shape is derived 

                     from a set of equations whose resulting out-

                     puts function as inputs for others.  Once the 

                     equations determining the control parameters 

                     have been set up it will be possible to create a 

                     new Feature based on these parameters that 

                     can be arrayed in a number of confi gurations 

                     to suit the potential design requirements.             136.  Chevron unit equations.

                     1.   Identifi cation of key parameters that will 

                          contribute to the functionality of the 

                          model and allow for the desired level of 

                          variability in the design.

                     According to mathematical equations devel-

                     oped based upon the Miura-ori pattern (Basily                                   "?WIDTH

                     2004a, p4-5) it was possible to create a num-

                     ber of graph variables that would allow for the 

                                                                                               &

                     creation of the dynamic chevron.  See Figures                                       (?HEIGHT

                     136 & 137.                                                !?LENGTH

                                                                                                  +

                                                                                                           #

                                                                                                                    %?THETA

                     2.   Development of the design model with                         6

                          a logical progression of generative fea-                      $?PHI

                                                                                                 '

                          tures.

                                                                                                   -

                     After resolution of the graph variables the next 

                     step was to begin creating control points that                   5

                     determine the vertices whose relative posi-

                     tions rely on the associative relationships of the     137.  One unit of chevron quintet with numeric 

                     graph variables.  With the knowledge that the          variables.

                                                                        117

## [p. 140]

chevron unit would be developed into a new 

                                                                                              GC chevron component Feature it was neces-

                                                                                              sary to develop a methodology for the repli-

                                                                                              cation and population of the chevron across 

                                                                                              a surface or defi ned area.  It was decided that 

                                                                                              the four facet chevron unit would be placed 

                                                                                              according to one control point and that sub-

                                                                                              sequent iterations of the chevron would use 

                                                                                              this point for their creation and placement.  

                                                                                              The base point was created at the (0, 0, 0) 

                                                                                              origin of the baseCS.  All of the subsequent 

                                                                                              points and facets are then based on their asso-

                                                                                              ciation to this point or points associated with 

                                                                                              it.  The derived points create what is essen-

                                                                                              tially a point cloud armature on which it was 

                                                                                              possible to develop the surface facets.   The 

                                                                                              facets were created between the appropri-

                                                                                              ate control points by using the Shape.By Ver-

                                                                                              tices feature.  This process was repeated three 

                                 138.  Progressive development of chevron facets.             additional times to create a four sided chevron 

                                                                                              unit which is able to be altered via manipu-

                                                                                              lation of the input values for the graph vari-

                                                                                              ables A_length, B_width, D_phi and E_theta.  

                                                                                              While this design exercise incorporates vari-

                                                                                              ability into all four of these values it is intended 

                                                                                              for ease of production that these values would 

                                                                                              not be continuously variable but would begin 

                                                                                              to form a line of discrete sizes available to the 

                                                                                              consumer similar to the standardization of siz-

                                                                                              ing for lumber, steel, and the like.  However, 

                                                                                              with the provision for variability the possibility 

                                 139.  Chevron inputs for update method.                      for custom production runs is still maintained.  

                                                                                              See Figure 138.

                                                                                              At this point the completed chevron was made 

                                                                                              into a new Feature in the same manner used 

                                                                                              in the creation of the chevron Feature in the 

                                                                                         118

## [p. 141]

140.  Population of baseCS with chevron components.

         141.  Dynamic movement of chevron units.

                                119

## [p. 142]

design 6.3.3 Static Deployment.  The inputs for 

                                                                                          the new Feature are a coordinate system, one 

                                                                                          corner point (BasePoint) for defi ning its loca-

                                                                                          tion, numerical values for the length and width 

                                                                                          of the individual chevron facet dimensions as 

                                                                                          well as numerical values that defi ne the angle 

                                                                                          of the chevron above the plane of the coordi-

                                                                                          nate system (E_theta) and angle (D_phi) defi n-

                                                                                          ing the shape of the physical chevron material 

                                                                                          from square (90 degrees) to a pronounced 

                                                                                          diamond (greater than 0 degrees) .  The fi rst 

                                                                                          angle will be infi nitely variable, from 0 degrees 

                                                                                          representing fully open to 90 degrees repre-

                                                                                          senting fully closed, which allows for dynamic 

                                                                                          folding of the chevron.  The second angle will 

                                                                                          be predetermined based on manufacturing 

                                                                                          requirements.  See Figure 139.

                                                                                          Once created, the completed chevron Fea-

                                142.  Symbolic view of chevron component derivation       ture can be replicated to create larger surfaces 

                                and relationships.                                        that are dynamic based upon the graph vari-

                                                                                          able values of E_theta which acts to fold and 

                                                                                          unfold the chevrons, and D_phi which repre-

                                                                                          sents the physical shape of the chevron facets.  

                                                                                          In a dynamic structure, E_theta would remain 

                                                                                          continuously variable and D_phi while variable 

                                                                                          in the development of the digital model would 

                                                                                          remain static after manufacturing has occurred.  

                                                                                          See Figures 140 & 141.

                                                                                          Figure 142 shows the complete symbolic view 

                                                                                          representing the progression from GraphVari-

                                                                                          ables to the chevron facets.  It is this assem-

                                                                                          bly that has been converted into a complete 

                                                                                          chevron feature for application to alternate 

                                                                                          surfaces.

                                                                                      120

## [p. 143]

6.3.4 Design Evaluation                                  parametric structural system has the abil-

                                                                             ity to update itself when necessary design 

                    Static Deployment                                        changes occur then a lot of time can be 

                                                                             saved with regard to recalculation and 

                    This design concept strived to develop a system          changes to support system location.  Any 

                    for populating complex surfaces with a struc-            additional requirements for either struc-

                    tural chevron form that can be derived from              ture, fi nishing or system integration could 

                    fl at sheets of CNC formed steel.  The idea was          thus be associated with the chevron fea-

                    based on the process of natural deployability,           ture and become instantly updateable as 

                    sensing and responding, self assembly and the            well.

                    power of shape.

                                                                        -    The chevron form used has been tested 

                    GenerativeComponents was once again used                 in a variety of loading and crushing tests 

                    extensively in the development of the chev-              (Basily 2004a) and has been found to out-

                    ron system.  As the system itself can adapt to           perform honeycomb panels in all direc-

                    a variety of surface confi gurations there is no         tions.  Depending on the application and 

                    defi nite fi nal form for evaluation which is pre-       size that the chevron system is to be pro-

                    cisely what was intended for the fi nal product.         duced there are a number of options that 

                                                                             can occur for ensuring proper rigidness.  

                    Advantages                                               Like honeycomb surfaces the ideal sce-

                                                                             nario would be to cover the chevrons with 

                    -   Throughout the development of a design,              a double layer of material that is bonded 

                        changes to the form of the exterior are              to the chevron substrate.  This application 

                        often necessary to accommodate for pro-              would be useful for aircraft applications, 

                        grammatic changes, budgetary require-                door panels, or interior wall partitions.  

                        ments among others.  In keeping with bio-            The requirement for the outer skin is to 

                        mimetic principles of design where all of            triangulate the pattern and overcome the 

                        the organism’s systems develop in unison             inherent fl exibility of the chevron material 

                        rather than in sequence it is benefi cial if         which may be cardboard, or a light gauge 

                        the architectural design can proceed in a            metal.  While not as strong as a dual skin, 

                        similar manner.  This means that all of the          it is possible to utilize a single sided stiff-

                        building systems should be integrated into           ening skin to allow exposure of the other 

                        the design from the outset.  The required            side for aesthetic purposes.  As the scale 

                        structural support for the building is of            of the chevrons increase to encompass 

                        immense importance and can have pro-                 a building façade it would be possible to 

                        found effects on the placement of other              use thicker plate steel that is much more 

                        systems such as HVAC.  In this case the              resistant to deformation and thus could 

                                                                    121

## [p. 144]

potentially resist the stresses on it without         required to produce the chevron system.  

                                   the need for a skin.                                  This is being addressed and will be con-

                                                                                         tained within future versions of the pro-

                              -    The unfolded chevron strips are derived               gram.

                                   from linear strips of fl at steel that are 

                                   cut and brake formed into their proper            -  The development of the transaction 

                                   confi guration.  The only requirement for             fi le that produced the chevron system 

                                   plasma or laser cutting would occur along             although satisfying the morphological 

                                   the exterior edges of the strips.  This slight        requirements set out in the brief fails to 

                                   zigzag cut pattern would effectively deter-           create the chevrons in a linear pattern 

                                   mine the location of the required bends               that would be able to be unfolded for 

                                   thus reducing manufacturing time.                     manufacturing.  The existing fi le creates 

                                                                                         arrays of each individual chevron facet of 

                              Areas for Development                                      the four part chevron unit.  Upon further 

                                                                                         development the transaction fi le will be 

                              -    With the exception of a planar surface,               refi ned to correct this.

                                   any other surface that the chevron sys-

                                   tem is applied to will result in chevrons of      -   The individual chevron facets developed 

                                   different shape and size.  Typical chevrons           in the program are realized by creating a 

                                   applied to a fl at surface will have facets           Shape based on vertices within the script.  

                                   that are of identical shape and size.  More-          These Shapes are contiguous and non-

                                   over the facets themselves will be planar.            planar relating to their proper confi gura-

                                   To effectively populate a complexly curved            tion.  When these shapes are turned into 

                                   surface the facets will be forced out of              Solids for export to STL for 3D printing 

                                   their planar confi guration.  While the abil-         the Shapes generated are non-contigu-

                                   ity of the chevron material to deform                 ous and planar which results in an incor-

                                   under these conditions may be relatively              rect model.  Further development of the 

                                   insignifi cant with thin gauge materials the          model will attempt to create the chevron 

                                   situation can intensify with thicker plate            facets out of BsplineSurfaces instead of 

                                   materials.  This potential problem can                Shapes which will allow for proper Solid 

                                   be reduced by increasing the number of                generation.

                                   chevrons or increasing the offset depth.

                                                                                     -   The current version of GC fails to unfold

## [p. 145]

Planning model for proper manufacturing.      -   Once the developed chevron model has 

                       Again, this should be remedied in future          been converted into a new Feature it is 

                       versions.                                         possible to replicate it over a desired sur-

                                                                         face.  Each independent chevron behaves 

                   Dynamic Deployment                                    the same way so that any changes made 

                                                                         will propagate throughout the entire 

                   This fi nal design concept is a slight departure      model.  This drastically reduces the time 

                   from the development of non-orthogonal                required in altering a design that requires 

                   structures in that its form is developed accord-      a large amount of units.

                   ing to mathematical formulas that ensure pla-

                   narity with respect to the chevrons.              Areas for Development

                   Advantages                                        -  The design developed here is derived 

                                                                         according to its relationship to the base 

                   -  The ability to create complex depen-               coordinate system rather than a surface 

                       dencies between variables examines the            situation.  This means that all instances of 

                       reductive instructional methods used in           the chevron feature must be contained 

                       nature.  By varying one Graph Variable            either on or in relation to the planar base 

                       within the set of variables it is possible not    coordinate system.  A progression of the 

                       only to dynamically alter the confi gura-         design to allow for the population of a 

                       tion of the design, but it also allows one        non-planar surface would require that 

                       to view the tangible changes that occur           its placement be dependent on a surface 

                       in all of the Graph Variables.  The prod-         rather than a coordinate system much like 

                       ucts of these values which can repre-             the static design scenario. 

                       sent areas, lengths, volumes, angles, or any 

                       other desirable are instantly available to    -   If the design is to conform to a non-planar 

                       the designer after every change occurs in         confi guration then it will also be necessary 

                       the model and can be exported to text             to integrate graph variables that allow for 

                       fi les or spreadsheets for further use.  For      a certain amount of material deformation 

                       example, the path that a point takes dur-         within the individual chevron facets.  The 

                       ing model deployment can be recorded              amount of deformation allowable would 

                       at a number of stages allowing a direction        be dependent on the material to be used 

                       path to be created that could be used for         as well as the native shape and size of 

                       the design of necessary mechanisms or             chevron to be used.  

                       linkages.

                                                                 123

## [p. 146]

_(página sin capa de texto)_

## [p. 147]

7.0    Discussion and Conclusion

                             125

## [p. 148]

7.1 Discussion                                        erful with regard to emulating the evolution-

                                                                                    ary adaptations present in natural design.  

                              This thesis sought to derive both a method 

                              and concepts for architectural design and con-        There is however a disjunction between the 

                              struction that take their inspiration from bio-       extensive period of time over which natural 

                              mimicry, essentially the “abstraction of good         evolution occurs versus the relatively short 

                              design from nature” (Aldersey-Williams 2006,          time period for development of architectural 

                              p168)  The key to an effective biomimetic             design works.  While GC allows for the simul-

                              investigation required the thoughtful selection       taneous progression of multiple designs, the 

                              of observed natural properties that satisfi ed a      quantitative and qualitative measure of these 

                              well defi ned list of desirables that were to be      designs in terms of a proven standard fall 

                              reached.                                              short of their natural counterparts that have 

                                                                                    had countless generations to arrive at their 

                              The concepts put forth in the thesis are valuable     native form.  The possibility for an accelerated 

                              in that they were produced through a rigorous         evolutionary digital design component arises 

                              approach to design based on fi nding solutions        with the prospect of using genetic algorithms 

                              for problems that were delineated at the out-         in conjunction with GC to produce and ana-

                              set of the investigation. This process allowed        lyze a much greater number of design alterna-

                              for the creation of designs that answered the         tives within the specifi ed design time available.  

                              question of what the design was to do rather          The inbuilt parametric variability of the chosen 

                              than what was to be designed. In approaching          design means that it remains active and appli-

                              the generation of the concepts in this man-           cable in other design scenarios where all of 

                              ner, the depth and transferability of the designs     the previous analysis and design time remains 

                              becomes greater, where one design can adapt           intact within the functionality of the specifi c 

                              to a multitude of different environments and          GC transaction script.  Subsequent designs 

                              scenarios. The adaptability of the design comes       then can be developed based on the outcome 

                              about through examining not only the design           and conclusions derived from previous designs 

                              but the process of design as well.  Parametric        thus promoting a continuous evolutionary 

                              design, namely in the form of the Generative-         design progression on a reduced timeframe.

                              Components design platform, was able to pro-

                              vide a framework for the concepts based on            A parallel between natural design possibilities 

                              the human genome that allowed them to be              and the limitation of GC exists, where the evo-

                              effectively developed both digitally and physi-       lution of natural organisms or digital designs 

                              cally. The innovative way in which Generative-        occurs within and not between possible out-

                              Components allows the designer to create              comes.  Humans exist in a variety of differ-

                              complex geometries while also giving provi-           ent confi gurations with regard to variability of 

                              sion for integrating design intent is very pow-       height, weight, color and many other charac-

                                                                                126

## [p. 149]

teristics.  However, all of these exist as varia-    ner, where a set of environmental conditions 

                     tions to a well defi ned template that is not        developed by the designer are created that 

                     variable, as occurs with bilateral symmetry and      mix different combinations of gene products, 

                     the reality of a homeothermic existence.  An         in the form of points, lines, arcs, etc, to arrive at 

                     extensive modifi cation to the human form or         a fi nal form.  By varying the conditions within 

                     systems with regard to the non-variable core         the script fi le, the designer is able to infl uence 

                     design aspects would constitute the develop-         the phenotype of the design without altering 

                     ment of a new species which would have fun-          the base genes that contain the formational 

                     damental differences that could not easily be        information.  In this way, GC provides an inter-

                     translated back into their original form.  With      esting corollary to the human genome in that 

                     regard to parametric design, GC contains lim-        the program itself contains the genetic infor-

                     itations within it with regard to the amount         mation to create specifi c gene components 

                     of design variability that can occur if not thor-    that when combined in a script fi le produce 

                     oughly thought out in the defi nition of the vari-   the desired building phenotype.  

                     ables and parameters of the design. If a plan is 

                     conceived of as a square, it cannot easily be        The correlation between the human genome 

                     changed parametrically into a circle.  Paramet-      and parametric design, in the form of GC, is 

                     ric software then is most useful in providing        successful in that provides a developmen-

                     variability within and not between design con-       tal design framework that allows designers 

                     cepts.  This point is crucial in determining at      to comprehend the vast possibilities available 

                     what point parametric design should enter the        with parametric design as well as providing 

                     design equation.  The designer must have a           strategies for their implementation.   This fact 

                     preconceived notion of how and in what form          is strengthened with the realization that the 

                     the fi nal product will take if they are to effec-   developmental and evolutionary limitations 

                     tively use GenerativeComponents throughout           inherent in the human genome have paral-

                     the design process.                                  leled the current limitations in GC and may 

                                                                          also provide markers and solutions for pos-

                     The human genome contains all of the infor-          sible problematic areas that may arise in the 

                     mation necessary to produce the gene prod-           future of GC development. 

                     ucts that derive the organism.  The fi nal form 

                     of the organism however is not contained             At present, GenerativeComponents is best 

                     within the genetic information, for it is in the     suited to the early stages of a design where 

                     interaction with the environment and between         a large amount of construction detail is not 

                     the various gene products that produce the           necessary.  It is envisioned that the system will 

                     respective phenotype.  The parametric aspect         continue to be developed to the point where 

                     of the script fi le contained within Generative-     it will be able to output the necessary con-

                     Components acts essentially in the same man-         struction information required for project 

                                                                      127

## [p. 150]

completion.  A true parametric design sys-             ture aids in resolving one subset of the larger 

                              tem would have the capacity to be relevant             architectural problem of linking all compo-

                              and contain a fully variable model complete            nents and systems of a design parametrically 

                              with as much construction detail as required.          along biomimetic principles.  

                              Additionally, the model would be able to be 

                              exported into all necessary AEC computation            The AEC community as a whole, much like 

                              software for analysis by all parties involved.         organisms in nature, must compete in an 

                              The advances in BIM have provided a relatively         increasingly competitive environment that 

                              robust parametric design environment, how-             rewards effi ciency and innovative approaches 

                              ever they approach parametric design in a dif-         that fi nd solutions to complex problems.  With 

                              ferent manner than GC.  The majority of BIM            this being the case it follows that in order to be 

                              software essentially creates smart objects that        competitive one must look at ways in which to 

                              carry with them geometric information for              reduce complexity and increase effi ciency not 

                              manufacturing, documentation and their loca-           only in the fi nal built form but in the way the 

                              tion within a building.  Parametric changes act        form is designed and built as well.   It should be 

                              on the level of individual elements which can          noted that the issue of competitiveness does 

                              in turn affect the other elements like it.  GC         not occur superfi cially between the resources 

                              has the ability to integrate changes beyond the        within fi rms of architects but more importantly 

                              individual element and widespread alterations          in the wholeness of their design solutions and 

                              can infl uence any number of desired elements.         the ability to perform extensive studies of 

                              When BIM and GC are able to effectively                design alternatives as necessary. The competi-

                              work together it will create a very robust and         tive aspect with regard to software innovation 

                              highly adaptive parametric design system that          and the tools available for design will diminish 

                              can be used throughout the entire design and           as they become widely accepted, therefore it 

                              construction process.                                  is in the process of design where fi rms will dif-

                                                                                     ferentiate themselves based on the nature of 

                              7.2 Conclusion                                         their design approach and therefore in how 

                                                                                     they use the tools available to them.  The well 

                              This thesis presents the development of a pro-         ordered, logical process of design, as illustrated 

                              cess for architectural design that parallels the       with the GenerativeComponents parametric 

                              way in which the human genome contains and             model based on the human genome, provides 

                              provides the information necessary for the             one type of platform that allows the designer 

                              creation of natural forms.  This process is illus-     to effectively develop and realize innovative 

                                                                                     design solutions.

                              trated with the use of parametric design soft-

                              ware in the form of GenerativeComponents,              Incorporation of parametric software into 

                              where its application to the design of curvilin-       the process of designing a project allows for 

                              ear architectural surfaces with integral struc-

                                                                                128

## [p. 151]

a design that derives its solutions through an        of information technology, states that “(in) a 

                     ordered developmental process acting in con-          conventional project each discipline’s design 

                     cert with an idea for the fi nal design concept.      intent is ambiguous to the others because they 

                     The ability of the architect to step forwards         use different symbology to represent building 

                     and backwards sequentially through a design           features and they don’t know enough of each 

                     as well as to pursue multiple variations of a         other’s design intent from a two-dimensional 

                     design simultaneously carries with it the abil-       drawing.  Designing from scratch in 3D means 

                     ity to drastically reduce the time invested in        no need to interpret, because the design 

                     exploring potential design alternatives while         intent and the features that would normally be 

                     increasing the time available to effectively          represented by symbols (are physically repre-

                     complete the design.                                  sented) as 3D objects.”  (Newton 2003)

                     Through the visualization of a project in a vari-     The ability to represent a design then not only 

                     ety of formats whether they be symbolic, 3D           in a 3D format but in a symbolic and trans-

                     model or transaction based, the designer is able      action based manner extends the ability of 

                     to structure the development of the design to         the designer to effectively communicate their 

                     parallel the possible modes of construction           design intent to all members of the AEC com-

                     that will be utilized. Once again the designer is     munity involved.  Again, the task of creating a 

                     able express their intent for the design much         design system that links all components of a 

                     like Gaudi and his contemporaries were able           design parametrically along biomimetic princi-

                     to do with their own.  In order to explain his        ples is aided in that the information necessary 

                     design for an innovative parabolic arch, Gaudi        for the realization of the design is available in a 

                     did not merely draw the form, rather he built         format that establishes and allows for a greater 

                     a hanging chain model where lines of ten-             cohesiveness and interoperability between 

                     sion become lines of pure compression when            design contributors.

                     inverted.  When draped with cloth, the chain 

                     represented a model of his arch.  He was able         In looking at the natural developmental process 

                     to use the most effi cient method available to        both in terms of coding and physical matura-

                     communicate his design intent to all of the           tion of an organism, the framework developed 

                     parties involved in the project.                      enables the designer to strategically assess the 

                                                                           requirements of a project and the relationship 

                     Paul Fletcher, co-founder of the Teamwork             of the design disciplines associated with it.  This 

                     Initiative which is a “learn by doing” consor-        aids in the creation of an effi cient work strat-

                     tium composed of members from the United              egy at every level of the design process. 

                     Kingdom’s most successful AEC fi rms that are 

                     seeking ways to document best practices in            The designer however, must be cognisant of 

                     collaboration and interoperability and the use        their limitations of digital design knowledge for 

                                                                      129

## [p. 152]

while it is possible to create an almost limitless     a number of morphological conditions with 

                              array of shapes and forms with the latest digi-        minimal user intervention.  From a design 

                              tal modeling software that can be easily trans-        standpoint the architect is able to invest more 

                              ferable between AEC contributors, it is quite          time in ensuring that the design works well as 

                              easy to allow the program itself to drive the          a cohesive and developed project as a whole 

                              morphology of the design.                              rather than manually deriving the individual 

                                                                                     units that must be created for its completion.  

                              Architect Greg Lynn outlined a number of               With time, the GenerativeComponents pro-

                              key points related to the way in which design-         gram could be populated with an increasing 

                              ers pursue their creativity and the methods            array of unique design components that could 

                              in which they use the computer to develop              act on various scales of the design from form 

                              them.  In a conversation with Yu-Tung Liu, Lynn        to detail thus compounding the effi ciency of 

                              stated that it is necessary to master a system         the design process.  

                              so that mastering succeeds, where creativity is 

                              not limited by knowledge of the system but             In concert with a well developed process for 

                              succeeds when the system becomes transpar-             architectural design, the thesis also puts forth 

                              ent.  He went on to state that design is an 

                              issue of mathematics and digital technology is         methods that reduce the complexity of the 

                              inherently sculptural and expressive.  In prac-        translation from the digital design to built 

                              tice, theory should precede technique. (Yu-            form.  The designs for curved building surfaces 

                              Tung Liu 2002)                                         with integral structure were able to be devel-

                                                                                     oped from linear and planar pieces of mate-

                              While parametric design is a powerful tool             rial that would require minimal processing to 

                              with which to create, organize and produce             achieve their fi nal form.  This has the benefi t of 

                              designs, it is in the way that the designs are         reducing the complexity of manufacturing and 

                              developed that is of crucial importance.  The          effectively reduces error and cost as a result.  

                              mathematical derivation of complex forms               The ability of GenerativeComponents to cre-

                              defi nes them in a way that can allow for a lay-       ate relevant manufacturing fi les directly from 

                              ering of complexity with regard to manufac-            the 3D model means that the time required 

                              ture and construction that would be more dif-          to produce or adjust shop drawings to refl ect 

                              fi cult in freely developed forms.  For example,       changes in a design is minimal.

                              the layout points, radii and other aspects of a 

                              mathematically derived curve can be easily cal-

                              culated within the program due to the nature           Finally, the conscious effort to derive struc-

                              of the curve itself.                                   tural components whose three dimensional 

                                                                                     conformation necessitates their orientation 

                              The formal success of the thesis design con-           and placement in a specifi c manner reduces 

                              cepts for curvilinear surfaces with integral           the number of construction drawings required 

                              structure lay in their ability to easily adapt to      and the possible confusion associated with 

                                                                                 130

## [p. 153]

the erection of the building.  With this being 

        the case, the contractors are able to be given 

        a small set of instructions specifying the pro-

        cess in which the pieces are to be assembled 

        rather than having to create an exhaustive set 

        of drawings that specify the location of each 

        piece.  In effect, the fi nal form of the compo-

        nents ensures a proper fi nal form of the struc-

        ture.

                          131

## [p. 154]

_(página sin capa de texto)_

## [p. 155]

Appendix

                          A1.  Design Concept #1 - GenerativeComponents Script File for 6.1.4.4 Illustrative Example  

                          transaction modelBased “Graph Variables Added”

                          {

                              feature GC.GraphVariable Building_Length

                              {

                                  Value                               = 10;

                                  UsesNumericLimits           = true;

                                  NumericLowLimit             = 5.0;

                                  NumericHighLimit            = 15.0;

                                  SymbolXY                            = {102, 102};

                              }

                              feature GC.GraphVariable Number_of_Floors

                              {

                                  Value                               = 5;

                                  SymbolXY                            = {98, 104};

                              }

                              feature GC.GraphVariable Floor_Height

                              {

                                  Value                               = 2;

                                  UsesNumericLimits           = true;

                                  NumericLowLimit             = 3.0;

                                  NumericHighLimit            = 4.0;

                                  SymbolXY                            = {98, 105};

                              }

                              feature GC.GraphVariable Building_Length

                              {

                                  NumericHighLimit            = 20.0;

                              }

                              feature GC.GraphVariable Building_Width

                              {

                                  Value                               = 10;

                                  UsesNumericLimits           = true;

                                  NumericLowLimit             = 5.0;

                                                                                       133

## [p. 156]

NumericHighLimit            = 20.0;

                                        SymbolXY                        = {102, 103};

                                    }

                                }

                                transaction modelBased “Point01 added”

                                {

                                    feature GC.Point point01

                                    {

                                        CoordinateSystem            = baseCS;

                                        Xtranslation                    = 0;

                                        Ytranslation                    = 0;

                                        Ztranslation                    = 0;

                                        SymbolXY                        = {99, 101};

                                    }

                                }

                                transaction modelBased “Line01 added”

                                {

                                    feature GC.Line line01

                                    {

                                        StartPoint                      = point01;

                                        Direction                       = baseCS.Xdirection;

                                        Length                          = Building_Length;

                                        SymbolXY                        = {99, 103};

                                    }

                                }

                                transaction modelBased “Building_Width GC value changed”

                                {

                                    feature GC.GraphVariable Building_Width

                                    {

                                        Value                           = Building_Length*0.5;

                                    }

                                }

                                transaction modelBased “Line02 added”

                                {

                                    feature GC.Line line02

                                    {

                                        StartPoint                      = point01;

                                                                                       134

## [p. 157]

Direction                         = baseCS.Ydirection;

                                Length                            = Building_Width;

                                SymbolXY                          = {101, 103};

                            }

                        }

                        transaction modelBased “Line03 offset from Line01”

                        {

                            feature GC.Line line03

                            {

                                OriginalLine                      = line01;

                                OffsetDistance                    = Building_Width;

                                PlaneOrPlanePoint                 = baseCS.Zdirection;

                                SymbolXY                          = {99, 104};

                            }

                        }

                        transaction modelBased “Line04 offset from Line02”

                        {

                            feature GC.Line line04

                            {

                                OriginalLine                      = line02;

                                OffsetDistance                    = Building_Length*(-1);

                                PlaneOrPlanePoint                 = baseCS.Zdirection;

                                SymbolXY                          = {101, 104};

                            }

                        }

                        transaction modelBased “Line05 added (represents all four vertical lines)”

                        {

                            feature GC.Line line05

                            {

                                StartPoint                        = {point01,line01.EndPoint,line02.EndPoint,line03.EndPoint};

                                Direction                         = baseCS.Zdirection;

                                Length                            = Floor_Height*Number_of_Floors;

                                SymbolXY                          = {100, 105};

                            }

                        }

                        transaction modelBased “line06 offset from line04”

                        {

                                                                                  135

## [p. 158]

feature GC.Line line06

                                      {

                                          OriginalLine                      = line04;

                                          OffsetDistance                    = Series(0,Floor_Height*Number_of_Floors,Floor_Height);

                                          PlaneOrPlanePoint                 = baseCS.YZplane;

                                          SymbolXY                          = {101, 106};

                                      }

                                      feature GC.Line line07

                                      {

                                          OriginalLine                      = line02;

                                          OffsetDistance                    = Series(0,Floor_Height*Number_of_Floors,Floor_Height);

                                          PlaneOrPlanePoint                 = baseCS.YZplane;

                                          SymbolXY                          = {99, 106};

                                      }

                                  }

                                  transaction modelBased “fl oor surfaces added”

                                  {

                                      feature GC.BsplineSurface bsplineSurface02

                                      {

                                          StartCurve                        = line07;

                                          EndCurve                           = line06;

                                          SymbolXY                          = {100, 107};

                                      }

                                  }

                                                                                           136

## [p. 159]

A2.  Design Concept #2 - GenerativeComponents Script File for Ruled Surface Structure

                          transaction modelBased “Graph Variable (Facade_Length)”

                          {

                              feature GC.GraphVariable Facade_Length

                              {

                                  Value                                 = 10;

                                  UsesNumericLimits                     = true;

                                  NumericLowLimit             = 1.0;

                                  NumericHighLimit            = 20.0;

                              }

                              feature GC.GraphVariable Line_Length

                              {

                                  Value                                 = 10;

                                  UsesNumericLimits           = true;

                                  NumericLowLimit             = 5.0;

                                  NumericHighLimit            = 10.0;

                                  SymbolXY                              = {103, 103};

                              }

                              feature GC.GraphVariable Primary_Sections

                              {

                                  Value                                 = 10;

                                  UsesNumericLimits           = true;

                                  NumericLowLimit             = 1.0;

                                  NumericHighLimit            = 20.0;

                              }

                              feature GC.GraphVariable Secondary_Sections

                              {

                                  Value                                 = 10;

                                  UsesNumericLimits           = true;

                                  NumericHighLimit            = 10.0;

                                  SymbolXY                              = {96, 106};

                              }

                              feature GC.GraphVariable Wall_Depth

                              {

                                  Value                                 = 2;

                                  UsesNumericLimits           = true;

                                                                                         137

## [p. 160]

NumericLowLimit             = 1.0;

                                        NumericHighLimit            = 5.0;

                                        SymbolXY                        = {96, 104};

                                    }

                                    feature GC.GraphVariable Wall_Height

                                    {

                                        Value                           = 10;

                                        UsesNumericLimits           = true;

                                        NumericLowLimit             = 5.0;

                                        NumericHighLimit                = 15.0;

                                        SymbolXY                        = {96, 104};

                                    }

                                }

                                transaction modelBased “Primary_Layout_Line (Base Line)”

                                {

                                    feature GC.Line Primary_Layout_Line

                                    {

                                        StartPoint                      = baseCS;

                                        Direction                       = baseCS.Xdirection;

                                        Length                          = Facade_Length;

                                        SymbolXY                        = {99, 101};

                                    }

                                }

                                transaction modelBased “cs01 (CS from baseCS)”

                                {

                                    feature GC.CoordinateSystem baseCS_Ztranslated

                                    {

                                        CoordinateSystem            = baseCS;

                                        Xtranslation                    = 0;

                                        Ytranslation                    = 0;

                                        Ztranslation                    = Wall_Height;

                                        SymbolXY                        = {102, 101};

                                    }

                                }

                                transaction modelBased “Primary_Layout_Line copy (from Base Line)”

                                {

                                    feature GC.Line Primary_Layout_Line_copy01

                                                                                       138

## [p. 161]

{

                                  FeatureToCopy                         = Primary_Layout_Line;

                                  From                                  = baseCS;

                                  To                                    = baseCS_Ztranslated;

                                  SymbolXY                              = {102, 102};

                              }

                          }

                          transaction modelBased “Secondary_Line_Layout_Points (Distribution of Points on Base Line)”

                          {

                              feature GC.Point Secondary_Line_Layout_Points

                              {

                                  Curve                                 = Primary_Layout_Line;

                                  NumberAlongCurve          = 5;

                                  SymbolXY                              = {97, 102};

                              }

                          }

                          transaction modelBased “Secondary_Layout_Line (Lines from Secondary_Line_Layout_Points)”

                          {

                              feature GC.Line Secondary_Layout_Line

                              {

                                  StartPoint                            = Secondary_Line_Layout_Points;

                                  Direction                             = baseCS.Ydirection;

                                  Length                                = Line_Length;

                                  SymbolXY                              = {100, 103};

                              }

                          }

                          transaction modelBased “Secondary_Layout_Line_Ztranslation (Copy of Secondary_Layout_

                          Line)”

                          {

                              feature GC.Line Secondary_Layout_Line_Ztranslation

                              {

                                  FeatureToCopy                         = Secondary_Layout_Line;

                                  From                                  = baseCS;

                                  To                                    = baseCS_Ztranslated;

                                  SymbolXY                              = {102, 104};

                              }

                          }

                                                                                         139

## [p. 162]

transaction modelBased “Bottom_Distances”

                                   {

                                       feature GC.Point Bottom_Distances

                                       {

                                           Curve                              = Secondary_Layout_Line;

                                           Distance                           = {5,1,4,6,2};

                                           SymbolXY                           = {100, 105};

                                       }

                                   }

                                   transaction modelBased “Top_Distances”

                                   {

                                       feature GC.Point Top_Distances

                                       {

                                           Curve                              = Secondary_Layout_Line_Ztranslation;

                                           Distance                           = {2,6,2,3,6};

                                           SymbolXY                           = {102, 105};

                                       }

                                   }

                                   transaction modelBased “Layout_Curves (Curves through Bottom and Top Distances)”

                                   {

                                       feature GC.BsplineCurve Layout_Curves

                                       {

                                           FitPoints                          = {Bottom_Distances,Top_Distances};

                                           SymbolXY                           = {101, 106};

                                       }

                                   }

                                   transaction modelBased “bsplineSurface01 (Through Layout_Curves)”, suppressed

                                   {

                                       feature GC.BsplineSurface bsplineSurface01

                                       {

                                           StartCurve                         = Layout_Curves[0];

                                           EndCurve                           = Layout_Curves[1];

                                       }

                                   }

                                   transaction modelBased “Primary_Planes (X section planes)”

                                   {

                                       feature GC.Plane Primary_Planes

                                                                                              140

## [p. 163]

{

                                Curve                                        = Primary_Layout_Line;

                                NumberAlongCurve                             = Primary_Sections;

                                NumberAlongCurveOption                       = null;

                                SymbolXY                                     = {99, 106};

                            }

                        }

                        transaction modelBased “point02 set (Intersection of Primary_Planes and bottom Layout_

                        Curves)”

                        {

                            feature GC.Point point02

                            {

                                Plane                              = Primary_Planes;

                                Curve                              = Layout_Curves[0];

                                SymbolXY                           = {99, 107};

                            }

                        }

                        transaction modelBased “point03 set (Intersection of Primary_Planes and top bsplineCurve02)”

                        {

                            feature GC.Point point03

                            {

                                Plane                              = Primary_Planes;

                                Curve                              = Layout_Curves[1];

                                SymbolXY                           = {101, 107};

                            }

                        }

                        transaction modelBased “Facade_Surface (From point set - point02 and point03)”

                        {

                            feature GC.BsplineSurface Facade_Surface

                            {

                                Points                             = {point03,point02};

                                SymbolXY                           = {100, 108};

                            }

                        }

                        transaction modelBased “Secondary_Planes (Y section planes)”

                        {

                            feature GC.Plane Secondary_Planes

                                                                                   141

## [p. 164]

{

                                           Curve                                        = Secondary_Layout_Line[2];

                                           NumberAlongCurve                             = Secondary_Sections;

                                           NumberAlongCurveOption                       = null;

                                           SymbolXY                                     = {98, 106};

                                       }

                                   }

                                   transaction modelBased “change in section variable”

                                   {

                                       feature GC.GraphVariable Secondary_Sections

                                       {

                                           Value                              = 15;

                                           NumericHighLimit            = 20.0;

                                       }

                                   }

                                   transaction modelBased “chevron skin”

                                   {

                                       feature GC.chevron_skin1 chevron_skin101

                                       {

                                           bsplineSurface02                   = Facade_Surface;

                                           Offset                    = 0.5;

                                           U_Variable                = .05;

                                           V_Variable                = .05;

                                       }

                                   }

                                   transaction modelBased “Section_Curves (Interesection of Secondary_Planes and bsplineSur-

                                   face01)”

                                   {

                                       feature GC.Curve Section_Curves

                                       {

                                           Plane                     = Secondary_Planes;

                                           Surface                   = Facade_Surface;

                                           SymbolXY                  = {98, 109};

                                       }

                                   }

                                   transaction modelBased “Graph changed by user”

                                   {

                                                                                              142

## [p. 165]

feature GC.BsplineSurface Facade_Surface

                            {

                                Display                   = DisplayOption.Hide;

                            }

                        }

                        transaction modelBased “change in section variable”

                        {

                            feature GC.GraphVariable Secondary_Sections

                            {

                                Value                     = 20;

                            }

                        }

                        transaction modelBased “Line03”

                        {

                            feature GC.Line line03

                            {

                                StartPoint                         = Secondary_Line_Layout_Points[0];

                                Direction                          = baseCS.Ydirection;

                                Length                             = 2;

                                SymbolXY                           = {97, 105};

                            }

                        }

                        transaction modelBased “line03 related to Graph Variable_Offset Length”

                        {

                            feature GC.Line line03

                            {

                                Length                             = Wall_Depth;

                            }

                        }

                        transaction modelBased “bsplineCurve02”

                        {

                            feature GC.BsplineCurve bsplineCurve02

                            {

                                FitPoints                          = {line03.StartPoint,line03.EndPoint};

                                SymbolXY                           = {97, 109};

                            }

                        }

                                                                                   143

## [p. 166]

transaction modelBased “bsplineSurface02 (Section Extrusions)”

                                       {

                                           feature GC.BsplineSurface bsplineSurface02

                                           {

                                                   Function  = function (Curves01,Direction01)

                                                               {

                                                              Print(Curves01.Count);

                                                               for (int i = 0; i <= Curves01.Count-1; i++)                                                   

                                                                          {

                                                                           Print(Curves01[i].Count);

                                                                          if(Curves01[i].Count==0)

                                                                          {

                                                                          BsplineSurface mySurface = CreateChildFeature(“BsplineSurface”,this);               

                                                                           mySurface.FromRailsAndSweptSections(Direction01,null, Curves01[i]);

                                                                           }

                                                                           else

                                                                          {

                                                                          for (int j = 0; j < Curves01[i].Count; ++j)

                                                                          {

                                                                           BsplineSurface mySurface = CreateChildFeature(“BsplineSurface”,this);

                                                                          mySurface.FromRailsAndSweptSections(Direction01,null,                                           

                                          Curves01[i][j]);

                                                                          }                                                                                                  

                                                                           }                                                                                

                                                                          }

                                                              };

                                                   FunctionArguments       = {Section_Curves,bsplineCurve02};

                                                   SymbolXY                    = {98, 111};

                                           }

                                       }

                                       transaction modelBased “Hide bsplineSurface01”, suppressed

                                       {

                                           feature GC.BsplineSurface bsplineSurface01

                                           {

                                               Display                                = DisplayOption.Hide;

                                           }

                                       }

                                                                                                        144

## [p. 167]

transaction modelBased “Change Wall_Depth”

                          {

                              feature GC.GraphVariable Wall_Depth

                              {

                                  Value                               = 1;

                              }

                          }

                          transaction modelBased “curve01_Vertical_Secondary_Sections”

                          {

                              feature GC.Curve Vertical_Secondary_Sections

                              {

                                  Plane                               = Primary_Planes;

                                  Surface                             = Facade_Surface;

                                  SymbolXY                            = {100, 109};

                              }

                          }

                          transaction modelBased “Section Curves (Intersection of plane 02 and bsplineSurface01)”

                          {

                              feature GC.BsplineSurface bsplineSurface03

                              {

                                     Function  = function (Curves02,Direction02)

                                     {

                                      {

                                      for (int i = 0; i <= Curves02.Count-1; i++)                                                               

                                      {

                                     BsplineSurface mySurface = CreateChildFeature(“BsplineSurface”,this);

                           mySurface.FromRailsAndSweptSections(Direction02,null, Curves02[i]);

                                     }                                                                                

                           }

                           };

                                  FunctionArguments         = {Vertical_Secondary_Sections,bsplineCurve02};

                                  SymbolXY                  = {100, 111};

                              }

                          }

                          transaction modelBased “Change Wall_Depth”

                          {

                              feature GC.GraphVariable Wall_Depth

                                                                                       145

## [p. 168]

{

                                             Value                               = 0.5;

                                             NumericLowLimit             = 0.5;

                                         }

                                     }

                                     transaction modelBased “New Model - Fabrication Planning and CS”

                                     {

                                         feature GC.CoordinateSystem Fabrication_Planning_Ruled_SurfaceBaseCS

                                         {

                                             Model                               = “Fabrication_Planning_Ruled_Surface”;

                                             SymbolXY                            = {103, 111};

                                         }

                                     }

                                     transaction modelBased “Shape01”, suppressed

                                     {

                                         feature GC.Shape shape01

                                         {

                                             Surface                             = Facade_Surface;

                                             Tolerance                           = 0.2;

                                             SymbolXY                            = {102, 110};

                                         }

                                     }

                                     transaction modelBased “Line01”

                                     {

                                         feature GC.Line line01

                                         {

                                             StartPoint                          = Secondary_Line_Layout_Points[0];

                                             Direction                           = baseCS.Zdirection;

                                             Length                              = Wall_Height;

                                         }

                                     }

                                     transaction modelBased “Point05”

                                     {

                                         feature GC.Point point05

                                         {

                                             Curve                               = Primary_Layout_Line;

                                             NumberAlongCurve          = Primary_Sections;

                                                                                                  146

## [p. 169]

}

                        }

                        transaction modelBased “Point07_Point_grid_on_Facade_Surface”, suppressed

                        {

                            feature GC.Point point07

                            {

                                CoordinateSystem            = baseCS;

                                Xtranslation                     = 0;

                                Ytranslation                     = 0;

                                Ztranslation                     = Series(0,Wall_Height,1);

                                Origin                           = point05;

                                Replication                      = ReplicationOption.AllCombinations;

                            }

                        }

                        transaction modelBased “Point06”, suppressed

                        {

                            feature GC.Point point06

                            {

                                Surface                                    = Facade_Surface;

                                PointToProjectOntoSurface                  = point07;

                                ProjectionVector                           = baseCS.Ydirection;

                            }

                        }

                        transaction modelBased “shape03”, suppressed

                        {

                            feature GC.Shape shape03

                            {

                                Points                           = point06;

                                Fill                             = true;

                            }

                        }

                        transaction modelBased “Graph changed by user”

                        {

                            feature GC.BsplineSurface Facade_Surface

                            {

                                Display                          = DisplayOption.Hide;

                            }

                                                                                147

## [p. 170]

feature GC.BsplineSurface bsplineSurface02

                                           {

                                                   Construction              = ConstructionOption.Construction;

                                           }

                                                   feature GC.BsplineSurface bsplineSurface03

                                           {

                                                   Construction              = ConstructionOption.Construction;

                                           }

                                       }

                                       transaction modelBased “fabricationPlanning01 in line with primary structure”, suppressed

                                       {

                                           feature GC.FabricationPlanning fabricationPlanning01

                                           {

                                               CoordinateSystem            = Fabrication_Planning_Ruled_SurfaceBaseCS;

                                               Shapes                                 = shape03;

                                               Xspacing                               = .25;

                                               Yspacing                               = .25;

                                               ForcePlanar                            = true;

                                           }

                                       }

                                       transaction modelBased “UV_points_on_surface”

                                       {

                                           feature GC.Point point01

                                           {

                                               Surface                                = Facade_Surface;

                                               U                                      = Series(0,1,0.1);

                                               V                                      = Series(0,1,0.1);

                                               Color                                  = 0;

                                               FillColor                              = -1;

                                               LineWeight                             = 0;

                                               LineStyle                              = 0;

                                               LineStyleName                          = “0”;

                                               Level                                  = 1;

                                               LevelName                              = “Level 1”;

                                               RoleInGraph                            = RoleInGraphOption.Output;

                                               RoleInExampleGraph                                 = null;

                                               RoleInComponentDefi nition                         = null;

                                                                                                        148

## [p. 171]

ComponentInput                                    = null;

                                   ComponentInputReplication                         = null;

                                   ComponentOutput                                   = null;

                                   Replication                                       = ReplicationOption.AllCombinations;

                                   Dynamics                                          = DynamicsOption.Dynamics;

                                   Update                                            = UpdateOption.Immediate;

                                   Construction                                      = ConstructionOption.Normal;

                                   Modify                                            = ModifyOption.Fixed;

                                   Display                                           = DisplayOption.Display;

                                   ConstructionDisplay                               = DisplayOption.Hide;

                                   DimensionDisplay                                  = DisplayOption.Hide;

                                   HandleDisplay                                     = DisplayOption.Hide;

                                   LabelDisplay                                      = LabelOption.Hide;

                                   MaximumReplication                                = true;

                                   Free                                              = true;

                                   ComponentDefi nitionInitialization   = null;

                                   SymbolXY                                          = {100, 109};

                                   SymbolicModelDisplay                              = null;

                                   ComputeGeometryInParameterSpace = null;

                               }

                           }

                           transaction modelBased “point04_UV_Points_on_Surface”

                           {

                               feature GC.Point point04

                               {

                                   Surface                                = Facade_Surface;

                                   U                                      = Series(0,1,0.1);

                                   V                                      = Series(0,1,0.1);

                               }

                               feature GC.Point point04

                               {

                                   Replication                            = ReplicationOption.AllCombinations;

                               }

                           }

                           transaction modelBased “Create text style”

                           {

                               feature GC.TextStyle Style01

                                                                                           149

## [p. 172]

{

                                           Height                              = 0.05;

                                           Width                               = 0.05;

                                           HeightOffset                        = 0.1;

                                           WidthOffset                         = 0.1;

                                           TextColor                           = 1;

                                       }

                                   }

                                   transaction modelBased “shape02_Place shapes on surface”

                                   {

                                       feature GC.Shape shape02

                                       {

                                           Points                              = point04;

                                           Fill                                = true;

                                           SkipAlternates                      = false;

                                           Facet                               = FacetOption.Quads;

                                           TextStyle                           = Style01;

                                       }

                                   }

                                   transaction modelBased “Turn construction display on”

                                   {

                                       feature GC.Shape shape02

                                       {

                                           ConstructionDisplay         = DisplayOption.Display;

                                       }

                                   }

                                   transaction modelBased “Layout shapes on unfold model”

                                   {

                                       feature GC.FabricationPlanning fabricationPlanning02

                                       {

                                           CoordinateSystem            = Fabrication_Planning_Ruled_SurfaceBaseCS;

                                           Shapes                              = shape02;

                                           Xspacing                            = 1;

                                           Yspacing                            = 1;

                                           TextStyle                           = Style01;

                                       }

                                   }

                                                                                               150

## [p. 173]

transaction modelBased “Turn on construction display”

        {

            feature GC.FabricationPlanning fabricationPlanning02

            {

                ConstructionDisplay         = DisplayOption.Display;

            }

        }

          

                          151

## [p. 174]

A3.  Design Concept #3A - GenerativeComponents Script File for Static Deployment - 

                                     Development of chevron_feature01

                                     transaction modelBased “Graph Variables”

                                     {

                                         feature GC.GraphVariable U_Variable

                                         {

                                             Value                               = 0.05;

                                         }

                                         feature GC.GraphVariable V_Variable

                                         {

                                             Value                               = 0.05;

                                         }

                                         feature GC.GraphVariable Offset

                                         {

                                             Value                               = 0.5;

                                         }

                                     }

                                     transaction modelBased “create bspline surf”

                                     {

                                         feature GC.Point point03

                                         {

                                             CoordinateSystem            = baseCS;

                                             Xtranslation                        = 0;

                                             Ytranslation                        = 4;

                                             Ztranslation                        = 0;

                                             HandleDisplay                       = DisplayOption.Display;

                                         }

                                         feature GC.Point point06

                                         {

                                             CoordinateSystem            = baseCS;

                                             Xtranslation                        = 4;

                                             Ytranslation                        = 4;

                                             Ztranslation                        = 0;

                                             HandleDisplay                       = DisplayOption.Display;

                                         }

                                         feature GC.Point point02

                                                                                                  152

## [p. 175]

{

                                CoordinateSystem            = baseCS;

                                Xtranslation                     = 0;

                                Ytranslation                     = 2;

                                Ztranslation                     = -2;

                                HandleDisplay                    = DisplayOption.Display;

                            }

                            feature GC.Point point05

                            {

                                CoordinateSystem            = baseCS;

                                Xtranslation                     = 4;

                                Ytranslation                     = 2;

                                Ztranslation                     = -2;

                                HandleDisplay                    = DisplayOption.Display;

                            }

                            feature GC.Point point04

                            {

                                CoordinateSystem            = baseCS;

                                Xtranslation                     = 4;

                                Ytranslation                     = 0;

                                Ztranslation                     = 0;

                                HandleDisplay                    = DisplayOption.Display;

                            }

                            feature GC.Point point01

                            {

                                CoordinateSystem            = baseCS;

                                Xtranslation                     = 0;

                                Ytranslation                     = 0;

                                Ztranslation                     = 0;

                                HandleDisplay                    = DisplayOption.Display;

                            }

                        }

                        transaction modelBased “bsplinecurve02,03 and bsplinesurface02”

                        {

                            feature GC.BsplineCurve bsplineCurve02

                            {

                                FitPoints                        = {point01,point02,point03};

                                                                                153

## [p. 176]

}

                                        feature GC.BsplineCurve bsplineCurve03

                                        {

                                            FitPoints                           = {point04,point05,point06};

                                        }

                                        feature GC.BsplineSurface bsplineSurface02

                                        {

                                            Curves                              = {bsplineCurve02,bsplineCurve03};

                                        }

                                    }

                                    transaction modelBased “UV points”

                                    {

                                        feature GC.Point point9

                                        {

                                            Surface                             = bsplineSurface02;

                                            U                                   = Series(0,1.01,U_Variable);

                                            V                                   = Series(0,1.01,V_Variable);

                                            Replication                         = ReplicationOption.AllCombinations;

                                        }

                                    }

                                    transaction modelBased “create point offsets”

                                    {

                                        feature GC.Point point10

                                        {

                                            Surface                             = bsplineSurface02;

                                            U                                   = Series(0,1.01,U_Variable);

                                            V                                   = Series(0,1.01,V_Variable);

                                            D                                   = Offset;

                                            Replication                         = ReplicationOption.AllCombinations;

                                        }

                                    }

                                    transaction modelBased “hide BsplineSurface and points9/10”

                                    {

                                        feature GC.BsplineSurface bsplineSurface02

                                        {

                                            Display                             = DisplayOption.Hide;

                                        }

                                                                                                154

## [p. 177]

feature GC.Point point9

                             {

                                 Display                            = DisplayOption.Hide;

                             }

                             feature GC.Point point10

                             {

                                 Display                            = DisplayOption.Hide;

                             }

                         }

                         transaction modelBased “lacing chevron 1”

                         {

                             feature GC.Shape shape27

                             {

                                 Function                           = function (refPtsA,refPtsB)

                             {

                                                                    for (value i = 0; i < refPtsA.Count; i=i+2)

                             {

                                                                                                      

                                                                                                     

                                               value shapeRow1 = CreateChildFeature(“Shape”,this);

                                               for (value j= 1; j < refPtsA.Count; j=j+2)

                                               {                                  

                           CreateChildFeature(“Shape”,shapeRow1).ByVertices({refPtsA[i][j],refPtsA[i+1][ 

                           j+1],refPtsB[i][j+1],refPtsB[i-1][j]}, true);

                           }

                           }

                           };

                                 FunctionArguments  = {point10,point9};

                             }

                         }

                         transaction modelBased “lacing chevron 2”

                         {

                             feature GC.Shape shape28

                             {

                                 Function = function (refPtsA,refPtsB)

                           {

                                               for (value i = 0; i < refPtsA.Count; i=i+2)

                                                                                     155

## [p. 178]

{ 

                                                               value shapeRow1 = CreateChildFeature(“Shape”,this);

                                                               for (value j= 1; j < refPtsA.Count; j=j+2)

                                         {

                                                                                                                      

                                         CreateChildFeature(“Shape”,shapeRow1).ByVertices({refPtsA[i][j],refPtsA[i+1][ 

                                         j-1],refPtsB[i][j-1],refPtsB[i-1][j]}, true);

                                         }

                                         }

                                        };

                                               FunctionArguments = {point10,point9};

                                           }

                                       }

                                       transaction modelBased “lacing chevron 3”

                                       {

                                           feature GC.Shape shape29

                                           {

                                               Function = function (refPtsA,refPtsB)

                                         {

                                                               for (value i = 1; i < refPtsA.Count; i=i+2)

                                         {

                                                               value shapeRow1 = CreateChildFeature(“Shape”,this);

                                                               for (value j= 1; j < refPtsA.Count; j=j+2)

                                         {

                                         CreateChildFeature(“Shape”,shapeRow1).ByVertices({refPtsB[i][j],refPtsB[i+1][j 

                                         -1],refPtsA[i][j-1],refPtsA[i-1][j]}, true);

                                                               }     

                                         }

                                        };

                                               FunctionArguments = {point10,point9};

                                           }

                                       }

                                       transaction modelBased “lacing chevron 4”

                                       {

                                           feature GC.Shape shape30

                                           {

                                               Function = function (refPtsA,refPtsB)

                                                                                                        156

## [p. 179]

{

                                                for (value i = 1; i < refPtsA.Count; i=i+2)

                            {

                                                value shapeRow1 = CreateChildFeature(“Shape”,this);

                                                for (value j= 1; j < refPtsA.Count; j=j+2)

                            {

                            CreateChildFeature(“Shape”,shapeRow1).ByVertices({refPtsB[i][j],refPtsB[i+1][j 

                            +1],refPtsA[i][j+1],refPtsA[i-1][j]}, true);

                                                }               

                            }

                           };

                                  FunctionArguments = {point10,point9};

                              }

                          }

                          transaction modelBased “Graph changed by user”

                          {

                              feature GC.GraphVariable Offset

                              {

                                  Value                               = 0.289;

                                  UsesNumericLimits           = true;

                                  NumericLowLimit             = 0.1;

                                  NumericHighLimit            = 1.0;

                          }

                          transaction modelBased “Graph changed by user”

                          {

                              feature GC.GraphVariable Offset

                              {

                                  Value                               = 0.181;

                                  UsesNumericLimits           = true;

                                  NumericLowLimit             = 0.1;

                                  NumericHighLimit            = 1.0;

                              }

                          }

                          transaction modelBased “Hide Shapes”

                          {

                              feature GC.Shape shape27

                              {

                                                                                       157

## [p. 180]

Display                            = DisplayOption.Hide;

                                        }

                                        feature GC.Shape shape28

                                        {

                                            Display                            = DisplayOption.Hide;

                                        }

                                        feature GC.Shape shape29

                                        {

                                            Display                            = DisplayOption.Hide;

                                        }

                                        feature GC.Shape shape30

                                        {

                                            Display                            = DisplayOption.Hide;

                                        }

                                    }

                                    transaction modelBased “Hide shape27”

                                    {

                                        feature GC.Shape shape27

                                        {

                                            Display                   = DisplayOption.Display;

                                        }

                                    }

                                    transaction modelBased “State at which new feature type, GC.chevron_feature01, created”

                                    {

                                    }

                                    }

                                                                                               158

## [p. 181]

A4.  Design Concept #3A - GenerativeComponents Script File for Static Deployment - 

                        Application of chevron_feature01 to Variable BsplineSurface

                        In this example, chevron_feature01 was applied to a BsplineSurface, where movement of the lay-

                        out points from point01 to point 07 produced the variety of forms displayed in Figure 135 on 

                        p116.

                        transaction modelBased “points”

                        {

                            feature GC.Point point07

                            {

                                CoordinateSystem            = baseCS;

                                Xtranslation                     = <free> (4.33763791286761);

                                Ytranslation                     = <free> (-2.13718670164055);

                                Ztranslation                     = <free> (6);

                                HandleDisplay                    = DisplayOption.Display;

                            }

                            feature GC.Point point06

                            {

                                CoordinateSystem            = baseCS;

                                Xtranslation                     = <free> (8.10086460967013);

                                Ytranslation                     = <free> (-3.89916514844596);

                                Ztranslation                     = <free> (4);

                                HandleDisplay                    = DisplayOption.Display;

                            }

                            feature GC.Point point05

                            {

                                CoordinateSystem            = baseCS;

                                Xtranslation                     = <free> (-2.02912063409083);

                                Ytranslation                     = <free> (18.6724857105255);

                                Ztranslation                     = <free> (0.0);

                                HandleDisplay                    = DisplayOption.Display;

                            }

                            feature GC.Point point04

                            {

                                CoordinateSystem            = baseCS;

                                Xtranslation                     = <free> (3.30917495547002);

                                                                                159

## [p. 182]

Ytranslation                      = <free> (16.9371610512656);

                                           Ztranslation                      = <free> (0.0);

                                           HandleDisplay                     = DisplayOption.Display;

                                       }

                                       feature GC.Point point03

                                       {

                                           CoordinateSystem            = baseCS;

                                           Xtranslation                      = <free> (5.53435513852012);

                                           Ytranslation                      = <free> (12.8185243895387);

                                           Ztranslation                      = <free> (0.0);

                                           HandleDisplay                     = DisplayOption.Display;

                                       }

                                       feature GC.Point point02

                                       {

                                           CoordinateSystem            = baseCS;

                                           Xtranslation                      = <free> (4.73560612610537);

                                           Ytranslation                      = <free> (6.9007426939103);

                                           Ztranslation                      = <free> (0.0);

                                           HandleDisplay                     = DisplayOption.Display;

                                       }

                                       feature GC.Point point01

                                       {

                                           CoordinateSystem            = baseCS;

                                           Xtranslation                      = <free> (0.223273654899217);

                                           Ytranslation                      = <free> (0.240351271830272);

                                           Ztranslation                      = <free> (0.0);

                                           HandleDisplay                     = DisplayOption.Display;

                                       }

                                   }

                                   transaction modelBased “Move points”

                                   {

                                       feature GC.Point point04

                                       {

                                           Xtranslation                      = <free> (1.02425502809233);

                                           Ztranslation                      = <free> (0.499971694588041);

                                       }

                                       feature GC.Point point05

                                                                                             160

## [p. 183]

{

                                Xtranslation                     = <free> (4.56675558979121);

                                Ytranslation                     = <free> (25.2348995107612);

                                Ztranslation                     = <free> (-0.540368485870081);

                            }

                        }

                        transaction modelBased “layout curves”

                        {

                            feature GC.BsplineCurve bsplineCurve02

                            {

                                FitPoints                        = {point05,point04,point03,point02,point01};

                            }

                            feature GC.BsplineCurve bsplineCurve01

                            {

                                FitPoints                        = {point01,point07,point06};

                            }

                        }

                        transaction modelBased “BsplineSurface”

                        {

                            feature GC.BsplineSurface bsplineSurface01

                            {

                                Rail0                            = bsplineCurve02;

                                Section0                         = bsplineCurve01;

                            }

                        }

                        transaction modelBased “Move points”

                        {

                            feature GC.Point point03

                            {

                                Xtranslation                     = <free> (3.62376586076137);

                            }

                            feature GC.Point point04

                            {

                                Xtranslation                     = <free> (1.24573118327263);

                                Ztranslation                     = <free> (0.0130934139742951);

                            }

                            feature GC.Point point05

                                                                                161

## [p. 184]

{

                                          Xtranslation                     = <free> (1.24524186693465);

                                          Ytranslation                     = <free> (28.8261168662667);

                                      }

                                      feature GC.Point point06

                                      {

                                          Xtranslation                     = <free> (6.1805308780735);

                                          Ytranslation                     = <free> (-5.41945972728544);

                                      }

                                      feature GC.Point point07

                                      {

                                          Xtranslation                     = <free> (-3.17996928267702);

                                          Ytranslation                     = <free> (2.41950379753293);

                                      }

                                  }

                                  transaction modelBased “chevron”

                                  {

                                      feature GC.chevron_feature chevron_feature01

                                      {

                                          bsplineSurface02                 = bsplineSurface01;

                                          Offset                           = -.5;

                                          U_Variable                       = 0.05;

                                          V_Variable                       = 0.05;

                                      }

                                  }

                                  transaction modelBased “Hide BSplineSurface01”

                                  {

                                      feature GC.BsplineSurface bsplineSurface01

                                      {

                                          Display                          = DisplayOption.Hide;

                                      }

                                  }

                                                                                           162

## [p. 185]

A5.  Design Concept #3B - GenerativeComponents Script File for Application of Dynamic 

                          Deployment

                          transaction modelBased “Create Graph Variables”

                          {

                              feature GC.GraphVariable A_length

                              {

                                  Value                               = 5;

                                  SymbolXY                            = {92, 106};

                              }

                              feature GC.Point BasePoint

                              {

                                  CoordinateSystem            = baseCS;

                                  Xtranslation                        = <free> (0);

                                  Ytranslation                        = <free> (0);

                                  Ztranslation                        = <free> (0.0);

                                  HandleDisplay                       = DisplayOption.Display;

                                  SymbolXY                            = {96, 102};

                                                                                       163

## [p. 186]

}

                                         feature GC.GraphVariable D_phi

                                         {

                                             Value                               = 39;

                                             UsesNumericLimits           = true;

                                             NumericHighLimit            = 180.0;

                                             SymbolXY                            = {95, 106};

                                         }

                                         feature GC.GraphVariable B_width

                                         {

                                             Value                               = 5;

                                             SymbolXY                            = {93, 106};

                                         }

                                         feature GC.GraphVariable E_theta

                                         {

                                             Value                               = 45;

                                             UsesNumericLimits           = true;

                                             NumericHighLimit            = 180.0;

                                             SymbolXY                            = {96, 106};

                                         }

                                         feature GC.GraphVariable H_height

                                         {

                                             Value                               = A_length*Sin(D_phi)*Sin(E_theta);

                                             SymbolXY                            = {95, 107};

                                         }

                                         feature GC.GraphVariable C

                                         {

                                             Value                               = A_length*Sin(D_phi);

                                             SymbolXY                            = {94, 106};

                                         }

                                         feature GC.GraphVariable M

                                         {

                                             Value                               = Atan(1/(Tan(D_phi)*Cos(E_theta)));

                                             SymbolXY                            = {97, 107};

                                         }

                                         feature GC.GraphVariable F

                                         {

                                                                                                  164

## [p. 187]

Value                               = Asin(Sin(D_phi)*Sin(E_theta));

                                  SymbolXY                            = {94, 107};

                              }

                              feature GC.GraphVariable G

                              {

                                  Value                               = B_width*Sin(D_phi);

                                  SymbolXY                            = {93, 107};

                              }

                              feature GC.GraphVariable K

                              {

                                  Value                               = Asin(Tan(F)/Tan(D_phi));

                                  SymbolXY                            = {96, 107};

                              }

                              feature GC.GraphVariable V

                              {

                                  Value                               = A_length*Cos(K);

                                  SymbolXY                            = {94, 108};

                              }

                              feature GC.GraphVariable U

                              {

                                  Value                               = B_width*Cos(M);

                                  SymbolXY                            = {93, 108};

                              }

                              feature GC.GraphVariable E_theta

                              {

                                  NumericHighLimit            = 90.0;

                              }

                              feature GC.GraphVariable D_phi

                              {

                                  Value                               = 45;

                                  NumericHighLimit            = 90.0;

                              }

                          }

                          transaction modelBased “Change BaseCS SymbolSize”

                          {

                              feature GC.CoordinateSystem baseCS

                              {

                                                                                       165

## [p. 188]

SymbolSize                       = .25;

                                         SymbolXY                         = {96, 100};

                                     }

                                 }

                                 transaction modelBased “V_point”

                                 {

                                     feature GC.Point V_Point

                                     {

                                         Origin                           = BasePoint;

                                         Direction                        = baseCS.Xdirection;

                                         Distance                         = V;

                                         SymbolXY                         = {92, 111};

                                     }

                                 }

                                 transaction modelBased “U_point”

                                 {

                                     feature GC.Point U_Point

                                     {

                                         Origin                           = BasePoint;

                                         Direction                        = baseCS.Ydirection;

                                         Distance                         = U;

                                         SymbolXY                         = {93, 111};

                                     }

                                 }

                                 transaction modelBased “cs_01”

                                 {

                                     feature GC.CoordinateSystem coordinateSystem01

                                     {

                                         Origin                           = BasePoint;

                                         CoordinateSystem            = baseCS;

                                         RotationAngle                    = -K;

                                         Axis                             = AxisOption.Y;

                                         SymbolXY                         = {94, 104};

                                     }

                                     feature GC.Point point12

                                     {

                                         Origin                           = BasePoint;

                                                                                         166

## [p. 189]

Direction                         = coordinateSystem01.Xdirection;

                                Distance                          = A_length;

                                SymbolXY                          = {94, 111};

                            }

                        }

                        transaction modelBased “cs_02”

                        {

                            feature GC.CoordinateSystem coordinateSystem02

                            {

                                Origin                            = BasePoint;

                                CoordinateSystem            = baseCS;

                                RotationAngle                     = 90-M;

                                Axis                              = AxisOption.Z;

                                SymbolXY                          = {98, 104};

                            }

                        }

                        transaction modelBased “point13”

                        {

                            feature GC.Point point13

                            {

                                Origin                            = BasePoint;

                                Direction                         = coordinateSystem02.Xdirection;

                                Distance                          = B_width;

                                SymbolXY                          = {95, 111};

                            }

                        }

                        transaction modelBased “point14”

                        {

                            feature GC.Point point14

                            {

                                Origin                            = point13;

                                Direction                         = coordinateSystem01.Xdirection;

                                Distance                          = A_length;

                                SymbolXY                          = {96, 111};

                            }

                        }

                        transaction modelBased “Chevron Face shape01”

                                                                                  167

## [p. 190]

{

                                        feature GC.Shape shape01

                                        {

                                            Vertices                            = {BasePoint,point12,point14,point13,};

                                            Fill                                = true;

                                            SymbolXY                            = {92, 114};

                                        }

                                    }

                                    transaction modelBased “Point_2U 2*U”

                                    {

                                        feature GC.GraphVariable Chevron_Width

                                        {

                                            Value                               = 2*U;

                                            SymbolXY                            = {93, 109};

                                        }

                                        feature GC.GraphVariable Chevron_Length

                                        {

                                            Value                               = 2*V;

                                            SymbolXY                            = {94, 109};

                                        }

                                        feature GC.Point Point_2U

                                        {

                                            Origin                              = BasePoint;

                                            Direction                           = coordinateSystem01.Ydirection;

                                            Distance                            = Chevron_Width;

                                            SymbolXY                            = {97, 111};

                                        }

                                    }

                                    transaction modelBased “point16 distance A from Point_2U”

                                    {

                                        feature GC.Point point16

                                        {

                                            Origin                              = Point_2U;

                                            Direction                           = coordinateSystem01.Xdirection;

                                            Distance                            = A_length;

                                            SymbolXY                            = {98, 111};

                                        }

                                                                                                168

## [p. 191]

}

                         transaction modelBased “Chevron face shape02”

                         {

                             feature GC.Shape shape02

                             {

                                 Vertices                            = {point13,point14,point16,Point_2U};

                                 Fill                                = true;

                                 SymbolXY                            = {95, 114};

                             }

                         }

                         transaction modelBased “Point_2V 2*V”

                         {

                             feature GC.Point Point_2V

                             {

                                 Origin                              = BasePoint;

                                 Direction                           = baseCS.Xdirection;

                                 Distance                            = 2*V;

                                 SymbolXY                            = {99, 111};

                             }

                         }

                         transaction modelBased “point18 distance B from Point_2V”

                         {

                             feature GC.Point point18

                             {

                                 Origin                              = Point_2V;

                                 Direction                           = coordinateSystem02.Xdirection;

                                 Distance                            = B_width;

                                 SymbolXY                            = {100, 111};

                             }

                         }

                         transaction modelBased “Point_2V_2U distance 2*V from Point_2U”

                         {

                             feature GC.Point Point_2V_2U

                             {

                                 Origin                              = Point_2U;

                                 Direction                           = baseCS.Xdirection;

                                 Distance                            = 2*V;

                                                                                      169

## [p. 192]

SymbolXY                        = {101, 111};

                                    }

                                }

                                transaction modelBased “Chevron face shape03”

                                {

                                    feature GC.Shape shape03

                                    {

                                        Vertices                        = {Point_2V,point12,point14,point18};

                                        Fill                            = true;

                                        SymbolXY                        = {98, 114};

                                    }

                                }

                                transaction modelBased “Chevron face shape04”

                                {

                                    feature GC.Shape shape04

                                    {

                                        Vertices                        = {Point_2V_2U,point18,point14,point16};

                                        Fill                            = true;

                                        SymbolXY                        = {101, 114};

                                    }

                                }

                                transaction modelBased “Line 2V”

                                {

                                    feature GC.Line Line_2Vto2V_2U

                                    {

                                        StartPoint                      = Point_2V;

                                        EndPoint                        = Point_2V_2U;

                                    }

                                }

                                transaction modelBased “State at which new feature type, GC.Chevron4, created”

                                {

                                }

                                transaction modelBased “Second Chevron Added”

                                {

                                    feature GC.GraphVariable E_theta

                                    {

                                        Value                           = 64.8;

                                                                                       170

## [p. 193]

}

                            feature GC.Chevron4 chevron401

                            {

                                A_length                          = 5;

                                B_width                           = 5;

                                BasePoint                         = Point_2U;

                                baseCS                            = baseCS;

                                D_phi                             = 60;

                                E_theta                           = E_theta;

                            }

                        }

                        transaction modelBased “Third Chevron Added”

                        {

                            feature GC.Chevron4 chevron402

                            {

                                A_length                          = 5;

                                B_width                           = 5;

                                BasePoint                         = Point_2V;

                                baseCS                            = baseCS;

                                D_phi                             = 60;

                                E_theta                           = E_theta;

                            }

                        }

                        transaction modelBased “Fourth Chevron Added”

                        {

                            feature GC.Chevron4 chevron403

                            {

                                A_length                          = 5;

                                B_width                           = 5;

                                BasePoint                         = Point_2V_2U;

                                baseCS                            = baseCS;

                                D_phi                             = 60;

                                E_theta                           = E_theta;

                            }

                        }

                                                                                  171

## [p. 194]

_(página sin capa de texto)_

## [p. 195]

Glossary

         Allele 

           Any one of a number of viable DNA codings occupying a given locus (position) on a 

             chromosome.  Usually alleles are DNA sequences that code for a gene, but sometimes 

             the term is used to refer to a non-gene sequence.  An individual’s genotype for that 

             gene is the set of alleles it happens to possess.  In a diploid organism, one that has two 

             copies of each chromosome, two alleles make up the individual’s genotype.  

         Diploid 

           Containing two sets of homologous chromosomes and hence two copies of each  

             gene or genetic locus. 

         Enzyme

           A protein functioning as a catalyst in living organisms, which promotes specifi c reactions or 

             groups of reactions.

         Genotype 

           Genetic constitution of an individual cell or organism, in the form of DNA.  Together with 

             the environmental variation that infl uences the individual, it codes for the phenotype of 

             the individual.  

         Microfi laments

           Helical protein fi lament formed by the polymerization of globular actin molecules.  A major 

             constituent of the cytoskeleton of all eucaryotic cells and part of the contractile appa-

             ratus of skeletal muscle.

          

         Microtubules

           Tubes that are the structural entity for eucaryotic fl agella, have a role in maintaining cell 

             shape, and function as mitotic spindle fi bers.

         Nucleotide

           Chemical compound that consists of a heterocyclic base, a sugar, and one or more 

             phosphate groups.  In the most common nucleotides the base is a derivative of purine 

             or pyrimidine, and the sugar is the pentose (fi ve-carbon sugar) deoxyribose or ribose.  

                             173

## [p. 196]

Nucleotides are the structural units of RNA, DNA, and several cofactors - CoA, FAD, 

              FMN, NAD, and NADP.  In the cell they play important roles in energy production, 

              metabolism, and signaling.

           Phenotype

             The phenotype of an individual organism is either its total physical appearance and 

              constitution or a specifi c manifestation of a trait, such as size, eye color, or behavior that 

              varies between individuals.  Phenotype is determined to some extent by genotype, or 

              by the identity of the alleles that an individual carries at one or more positions on the 

              chromosomes.  Many phenotypes are determined by multiple genes and infl uenced by 

              environmental factors.  Thus, the identity of one or a few known alleles does not always 

              enable prediction of the phenotype. 

           Polypeptide

             Linear polymer composed of multiple amino acids.  Proteins are large polypeptides, and the 

               two terms can be used interchangeably.  

                             174

## [p. 197]

References

         Aalbers, Cas, H.  Bier, S.  Boer, and K.  Oosterhuis. 2004.  File to factory and real-time behaviour in 

           ONL-architecture.  Paper presented at Fabrication: examining the digital practice of architecture, 

           Cambridge & Toronto. 

         Aish, R.  2004.  Generative Components Introduction:  Bentley Institute Course Guide.  Bentley Sys-

           tems, Incorporated.

         Alberts, B., D. Bray, J. Lewis, M. Raff, K. Roberts, and J. Watson. 1994.  Molecular Biology of the Cell.  

           3rd edition ed. New York, NY: Garland Publishing.

         Aldersey-Williams, H.  2003.  New animal architecture.  London: Laurence King Publishing. 

         Anders, P., and M. Phillips.  2004.  Arch-OS: An operating system for buildings.  Paper presented at Fab-

           rication: examining the digital practice of architecture, Cambridge & Toronto.

         Ban, Shigeru. 2000.  Projects in process to japanese pavilion, expo 2000 hannover.  2nd Edition ed. 

           Tokyo: Mitsuo Kawagoe. 

         Basily, B. B., and E. A. Elsayed.  2004a.  A continuous folding process for sheet materials.  International 

           Journal of Materials and Product Technology 21, (1/2/3): 217-238. 

         ----------. 2004b.  Dynamic axial crushing of multi-layer core structures of folded chevron patterns.  

           International Journal of Materials and Product Technology 21, (1/2/3): 169-185. 

         Batcheler, B., and I. Howell.  Building information modeling two years later - huge potential, some suc-

           cess and several limitations.  in The Laiserin Letter [database online]. 20052006].  Available 

           from http://www.laiserin.com/features/bim/newforma_bim.pdf. 

         Beesley, P., R. MacHenry, and E. von Michalofski.  2001.  On growth and form - textiles and the engi-

           neering of nature.  Toronto: Textile Museum of Canada. 

         Bell, B., and A. Vrana.  2004.  Digital Tectonics:  Structural Patterning of Surface Morphology.  Fabrication: 

           examining the digital practice of architecture.  Cambridge & Toronto. 

                             175

## [p. 198]

Benyus, J. 1997. Biomimicry: Innovation inspired by nature. 1st Edition ed. New York, NY: William 

             Morrow.

           Benyus, J.  2004.  Biomimicry.  Pop!Tech Lecture Series.  Camden, Maine.  Recorded Oct. 22, 2004.

           Biomimicry Guild.  Biomimicry methodology.  2006 [cited 06/21 2005].  Available from http://www.

             biomimicry.net/essent_resourc.html. 

           Brock, T., M. Madigan, J. Martinko, and J. Parker.  1994.  Biology of microorganisms.  New Jersey: Pren-

             tice Hall.

           Burry, Mark. 1999.  Paramorph.  Architectural Design 69, (10): 78-83. 

           Coffey, J.  Automating thermal plate forming for hull plates. in The Navy Joining Center [database 

             online]. Columbus, Ohio, 2006].  Available from http://www.ewi.org. 

           Coop Himmelb(l)au.  Seoul performing arts center.  [cited 09/15 2005].   Available from http://www.

             emergentarchitecture.com/projects.php?id=8.  

           Craven, J.  Master Architects:  Antoni Placid Guillem Gaudi Cornet.  [cited 05/01 2006].  Available from 

             http://architecture.about.com/library/blgaudi.htm.  

           DECOI: Goulthorpe, Mark.  1999.  Aegis hyposurface autoplastic to alloplastic.  Architectural Design 

             69, (10): 60-65. 

           Denton, M., and C. Marshall.  2001.  Laws of form revisited. Nature 410, (March 22): 417. 

           Edwardson, S. 2003. High-powered laser forming of metallic components. Dies and Stamping 

             News(April), http://www.lasers.org.uk/paperstore/Forming4.pdf. 

           EMERGENT Architecture.  Lattice house.  [cited 09/15 2005a].  Available from http://www.emer-

             gentarchitecture.com/projects.php?id=9.  

           ----------. Radiant hydronic house.  [cited 09/15 2005b].  Available from http://www.emergentarchi-

             tecture.com/projects.php?id=7. 

                             176

## [p. 199]

Faludi, J.  Biomimicry for green design (A how-to).  2006 [cited 10/28 2005].  Available from http://

          www.worldchanging.com/archives/003680.html#more. 

        Forbes, P.  2000.  Folders fi nd a new wrinkle.  Guardian (Thursday, November 23), http://www.guard-

          ian.co.uk. 

        Forte, C.  Packaging material innovation: 3-D folded structures.  2005 [cited 01/05 2006].  Available 

          from http://www.iopp.org/fi les/Forte_Chris_Rutgers_3D_Structures.pdf?pageid=pageid. 

        Foster, N., D. Sudjic, and S. de Grey.  2001.  Norman foster and the british museum. New York: Pre-

          stel. 

        Gallaher, M., A. O’Connor, J. Dettbarn, and L. Gilday.  2004.  Cost analysis of inadequate interoperabil-

          ity in the U.S. capital facilities industry.  Gaithersburg, Maryland.: U.S. Department of Commerce 

          Technology Administration.  National Institute of Standards and Technology., NIST GCR 04-

          867. 

        Godfaurd, J., D. Clements-Croome, and G. Jeronimidis.  March 2005.  Sustainable building solutions: 

          A review of lessons from the natural world.  Building and Environment 40, (3): 319. 

        Goodsell, D.  1996.  Our Molecular Nature: The Body’s Motors, Machines, and Messages.  New York: 

          Springer-Verlag.

        Haas, F.  1998.  Wing folding in insects: A natural, deployable structure.  Paper presented at IUTAM-

          IASS Symposium on Deployable Structures: Theory and Applications, Cambridge, UK. 

        Hall, P.  2003.  Bend the rules of structure: A brooklyn metalworking shop with an unlikely name may 

          hold the key to 21st century shapemaking.  Metropolis. 

        Jirapong, K., and R. Krawczyk.  2002.  Architectural forms by abstracting nature.  Paper presented at 

          Generative Art Conference, Milan, Italy. 

        Kilian, A.  2004.  Linking digital hanging chain models to fabrication.  Paper presented at Fabrication: 

          examining the digital practice of architecture, Cambridge & Toronto. 

        Knecht, B.  Brave new solid-state, carbon fi ber world.  [cited 06/15 2005].  Available from http://

          archrecord.construction.com/innovation/2_Features/0310carbonfi ber.asp

                          177

## [p. 200]

_(página sin capa de texto)_

## [p. 201]

Pearson, David.  2001.  New Organic Architecture:  The Breaking Wave.  University of California 

          Press.   

        Perez, S.  2004.  The synthetic sublime - notes on physical/digital space and form.  Paper presented at 

          Fabrication: examining the digital practice of architecture, Cambridge & Toronto. 

        Portoghesi, Paolo.  April 30, 2006.  Concrete architecture.  Materia(No. 46), http://www.materia.

          it/materia. 

        Pottman, H, and J. Wallner.  2001.  Computational line geometry.  Mathematics and visualization., eds.  

          Gerlad Farin, Hans-Christian Hege, David Hoffman, Christopher R. Johnson and Konrad Pol-

          thier.  New York: Spinger-Verlag. 

        Sanders, K.  2004.  Why building information modeling isn’t working...yet.  Architectural Record, http://

          archrecord.construction.com/features/digital/archives/0409feature-1.asp. 

        Schlaich, J., H. Schober, and K. Kurschner.  2005.  New trade fair in milan - grid topology and structural 

          behaviour of a free-formed glass-covered surface. International Journal of Space Structures 20, 

          (1): 1-14. 

        Schodek, D., M. Bechtold, K. Griggs, K. Martin,  and M. Steinberg.  2005.  Digital Design and Manufac-

          turing - CAD/CAM Applications in Architecture and Design.  New Jersey: John Wiley & Sons.

        Schrodinger, E.  1944.  What is life? the physical aspect of the living cell.  Cambridge: Cambridge 

          University Press. 

        Seebohm, T., and W. Wallace.  1998.  Rule-based representation of design in architectural practice.  

          Automation in Construction 8, : 73. 

        Spuybroek, Lars.  2004a.  D-tower.  In NOX machining architecture., 158.  New York, NY: Thames 

          & Hudson. 

        ----------.  2004b. ECB.  In NOX machining architecture., 290.  New York, NY: Thames & Hudson. 

        ----------.  2004c. obliqueWTC.  In NOX machining architecture., 260.  New York, NY: Thames & 

          Hudson. 

                          179

## [p. 202]

----------.  2004d.  OffTheRoad_5Speed.  In NOX machining architecture., 114.  New York, NY: 

             Thames & Hudson. 

           ----------.  2004e.  Pompidou two.  In NOX machining architecture., 304.  New York, NY: Thames 

             & Hudson. 

           ----------.  2004f.  Soft offi ce.  In NOX machining architecture., 216.  New York, NY: Thames & Hud-

             son. 

           ----------.  2004g.  Son-O-house.  In NOX machining architecture., 174.  New York, NY: Thames & 

             Hudson. 

           ----------.  2004h.  wetGRID.  In NOX machining architecture., 139.  New York, NY: Thames & Hud-

             son. 

           Srinivasan, A. V.  March 1996. Smart biological systems as models for engineered structures.  Materials 

             Science & Engineering: C 4, (1): 19. 

           Thompson, D.  1963.  On growth and form.  2nd Edition, reprinted ed. Vol. 1.  Deventer, Holland: 

             Cambridge University Press. 

           Tsui, E.  1999.  Evolutionary architecture - nature as a basis for design.  New York: John Wiley & 

             sons. 

           ----------.  Tsui design & research inc.  2006.  Available from http://www.tdrinc.com/.  2006.

           Vincent, J.  2002.  Deployable structures, ed. S. Pellegrino. 1st Edition ed. Vol. Vol. 1. Vienna: Springer.

            

           Vogel, S.  1998.  Cat’s paws and Catapults.  Mechanical worlds of nature and people.  1st Edition.  

             New York: W.W. Norton & Company.

           Vollers, K.  2001.  Twist & build creating non-orthogonal architecture.  Trans. Lynn de Graaf and 

             Brenda Vollers-King.  Rotterdam: 010 Publishers. 

           Wade, L. G., Jr.  1995.  Organic chemistry.  3rd Edition ed.  New Jersey: Prentice Hall.

                             180

## [p. 203]

Weinstock, M.  2004.  Morphogenesis and the Mathematics of Emergence.  Architectural Design Vol 

          74; Part 3, p10-17.  Great Britain: Academy Group Ltd.

        Whitesides, G., Gryboski, B.  2002.  Self Assembly at All Scales.  Science 29 March.  Vol. 295, no. 5564.

          p.2418-2421

        Yeang, K.  2002.  Reinventing the Skyscraper:  A Vertical Theory of Urban Design.  New Jersey:  

          John Wiley & Sons.

                          181
