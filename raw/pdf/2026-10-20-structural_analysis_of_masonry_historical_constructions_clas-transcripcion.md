---
tipo: transcripcion
fecha: 2026-10-20
fuente_binaria: activos/fuentes/structural_analysis_of_masonry_historical_constructions_clas/Structural Analysis of Masonry Historical Constructions. Classical and Advanced Approaches.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Structural Analysis of Masonry Historical Constructions. Classical and Advanced Approaches.pdf
titulo: Structural Analysis of Historical Constructions
autor: Pere Roca 2
idioma: en
paginas: 42
palabras: 13069
metodo_extraccion: ghostscript-txtwrite
aviso: "Texto con copyright - uso interno del estudio. Citar con atribucion; no redistribuir."
tags: [pdf, raw, transcripcion, gaudi, bibliografia-ai, fair-use]
---

# Transcripción — Structural Analysis of Historical Constructions

> Texto extraído para análisis interno del estudio. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Structural Analysis of Masonry Historical Constructions. Classical and Advanced Approaches.pdf`. Binario local: [activos/fuentes/structural_analysis_of_masonry_historical_constructions_clas/Structural Analysis of Masonry Historical Constructions. Classical and Advanced Approaches.pdf].
> Extracción: ghostscript-txtwrite · 42 págs · 13069 palabras. Copyright del original: se cita con atribución, no se redistribuye.

## [p. 1]

1 

          

            Structural Analysis of Masonry Historical Constructions. 

                  Classical and Advanced Approaches 

                  Pere Roca, Miguel Cervera, Giuseppe Gariup, Luca Pelà 

                      Universitat Politècnica de Catalunya 

          

         Pere Roca, Professor 

         Technical University of Catalonia, Jordi Girona 1-3, 08034 Barcelona, Spain 

         pere.roca.fabregat@upc.edu 

          

         Miguel Cervera, Professor 

         Technical University of Catalonia,  Jordi Girona 1-3, 08034 Barcelona, Spain 

         miguel.cervera@upc.edu 

          

         Giuseppe Gariup, Ph. D. candidate 

         Technical University of Catalonia, Jordi Girona 1-3, 08034 Barcelona, Spain 

         giuseppe.gariup@upc.edu 

          

         Luca Pelà, Research Assistant 

         University of Bologna, Bologna, Italy 

         luca.pela@unife.it 

          

          

         Abstract 

         A review of methods applicable to the study of masonry historical construction, encompassing 

         both classical and advanced ones, is presented.  Firstly, the paper offers a discussion on the main 

         challenges posed by historical structures and the desirable conditions that approaches oriented 

         to the modeling and analysis of this type of structures should accomplish. Secondly, the main 

         available methods which are actually used for study masonry historical structures are referred to 

         and discussed.  

         The main available strategies, including limit analysis, simplified methods, FEM macro- or micro-

         modeling and discrete element methods (DEM) are considered with regard to their  realism, 

         computer efficiency, data availability and real applicability to large structures.  A set of final 

         considerations are offered on the real possibility of carrying out realistic analysis of complex 

         historic masonry structures. In spite of the modern developments, the study of historical buildings 

         is still facing significant difficulties linked to computational effort, possibility of input data 

         acquisition and limited realism of methods.   

          

         Keywords  

         Historical construction, structural analysis, masonry mechanics, limit analysis, macro-modeling, 

         micro-modeling, discontinuous methods.

## [p. 2]

2 

          

            Structural Analysis of Masonry Historical Constructions. 

                  Classical and Advanced approaches 

                  Pere Roca, Miguel Cervera, Giuseppe Gariup, Luca Pelà 

                      Universitat Politècnica de Catalunya 

          

          

         1. Introduction.  Purpose and challenges 

          

         Studies oriented to conservation and restoration of historical structures have recourse  to 

         structural analysis as a way to better understand the genuine structural features of the building, 

         to characterize its present condition and actual causes of existing damage, to determine the true 

         structural safety for a variety of actions (such as gravity, soil settlements, wind and earthquake) 

         and to conclude on necessary remedial measures. In short, structural analysis contributes to all 

         the phases and activities (including diagnosis, reliability assessment and design of intervention) 

         oriented to grant an efficient and respectful conservation of monuments and historical buildings. 

         Accurate structural analysis is needed to avoid erroneous or defective conclusions leading to 

         either over-strengthen the structure, causing unnecessary loss in terms of original material and 

         cultural value, or to insufficiently intervene on it, and hence generate inadmissible risks on people 

         and heritage. Unsurprisingly, ancient structures have been studied, since long time ago, using 

         the most advanced tools available for structural assessment.  

          

         The application of advanced computer methods to the analysis of historical structures was 

         pioneered by the studies of the Brunelleschi Dome by Chiarugi et al. (1993), the Pisa Tower by 

         Macchi et al. (1993), the Colosseo in Rome by Croci (1995), see also Croci and Viskovic (1993), 

         Mexico Cathedral by Meli and Sánchez-Ramírez (1995) and San Marco’s Basilica in Venice by 

         Mola and Vitaliani (1995), among others (Figs.1 and 2). By then, the development of methods for 

         accurate analysis of steel and concrete structures, including non-linear applications, was already 

         at a very advanced stage thanks to the work of Zienkiewicz and Taylor (1991), Ngo and Scordelis 

         (1964) and many others. Notwithstanding, analysts attempting to use computer tools for the study 

         historical structures were by then facing overwhelming challenges. Methods then available were 

         not yet prepared to tackle the specific problems of ancient constructions concerning materials, 

         structural arrangements and real preservation condition. In fact, the difficulties posed by historical 

         structures are still very challenging, and still reminiscent of those encountered by the pioneers, in 

         spite of significant progress during the last decades.  

                                             

         Some of difficulties encountered are related to the description of geometry, materials and actions, 

         all of which acquire remarkable singularity in the case  of historical construction. Additional 

         important difficulties are related to the acquisition  of data on material properties, internal 

         morphology and damage, as well as to the adequate interpretation of structural arrangements, 

         overall organization and historical facts. Because of all these difficulties, it is generally accepted 

         (Icomos/Iscarsah Committee, 2005) that the study of a historical structure should not only base 

         on calculations, but should integrate as well a variety of complementary activities involving 

         detailed historical investigation, deep inspection by means of non destructive techniques (NDT) 

         and monitoring, among other. Structural analysis of historical structures constitutes in fact a 

         multidisciplinary, multifaceted activity requiring a clever integration of different approaches and 

         sources of evidence. These difficulties are discussed into more detail in the following paragraphs.  

          

          

         1- Material. Historical or traditional materials such as earth, brick or stone masonry and wood are 

         characterized by very complex mechanical and strength phenomena still challenging our

## [p. 3]

3 

          

         modeling abilities. In particular, masonry is characterized by its composite character (it includes 

         stone or brick in combination with mortar or day joints), a brittle response in tension (with almost 

         null tensile strength), a frictional response in shear (once the limited bond between units and 

         mortar is lost) and anisotropy (for the response is highly sensitive to the orientation of loads). In 

         spite of the very significant effort invested to characterize and mathematically describe masonry 

         mechanics and strength, the accurate and efficient simulation of masonry response is still a 

         challenge in need of further experimental and theoretical developments. Important results by Ali 

         and Page (1988), Lourenço (1996), Binda et al. (1997) and many others have yielded a very 

         significant level of understanding.   

          

         Historical materials, including brick or stone masonry, are normally very heterogeneous even in 

         a single building or construction member. Moreover, historical structures often show many 

         additions and repairs done with different materials. Material characterization is constrained by 

         due respect to the monument and original material. Non- destructive, indirect, tests (NDT) and 

         minor destructive tests (MDT) should be preferred. If any, only a very limited number of pits or 

         cores allowing direct observation and laboratory testing are normally acceptable. In practice, only 

         limited and partial information can be collected. Additional assumptions on morphology and 

         material properties may be needed in order to elaborate a model. 

          

         2- Geometry. Historical structures are often characterized by a very complex geometry. They 

         often include straight or curved members. They combine curved 1D members (arches, flying 

         arches) with 2D members (vaults, domes) and 3D ones (fillings, pendentives…). They combine 

         slender members with massive ones (massive piers, walls buttresses, foundations…).  However, 

         today numerical methods (such as FEM) do afford a realistic and accurate description of 

         geometry. Due to it, geometry is perhaps one of the least (although still meaningful) challenges 

         to be faced by the analysis.  

          

         3. Morphology. A more significant problem lays in the characterization and description of the 

         internal morphology of structural members and their connections. Structural members are often 

         non-homogeneous and show complex internal structures including several layers, filling, material, 

         cavities, metal insertions and  other possible singularities.  Connections are singular regions 

         featuring specific geometric and morphological treats. The transference of forces may activate 

         specific resisting phenomena (contact problems, friction, eccentric loading). Modeling morphology 

         and connections in detail may be extremely demanding from a computational point of view.  

         Nevertheless, the main difficulty is found in physically characterizing them by means of minor- or 

         non-destructive procedures. 

          

         4. Actions. Historical structures may have experienced (and keep on experiencing) actions of 

         very different nature, including the effects of gravity forces in the long term, earthquake, 

         environmental effects (thermal effects, chemical or physical attack), and anthropogenic actions 

         such as architectural alterations, intentional destruction, inadequate restorations… Many of these 

         actions are to be characterized in historical time. Some are cyclic and repetitive (and accumulate 

         significant effect in the long term), some develop gradually in very long time periods, and some 

         are associated to long return periods. In many cases, they may be influenced by historical 

         contingency and uncertain (or at least, insufficiently known) historical facts.

## [p. 4]

4 

          

                                         (a)  

                                  (b) 

                                       (c) 

         Fig. 1: Some pioneering FEM studies on historical structures. (a) Tower of Pisa: FEM model and 

         substructuring of the colonnade system (Macchi et al, 1993). (b) Mexico City Cathedral (Meli and 

         Sánchez Ramírez, 1995). (c) The Colosseum in Rome. Tensile horizontal stresses due to the 

         seismic action (Croci, 1995).

## [p. 5]

5 

          

         5. Damage and alterations. Existing and general alterations may affect very significantly the 

         response of the structure.  Damage and deformation are to be modeled, as present features of 

         any existing structure, to grant adequate realism and accuracy in the prediction of the actual 

         performance and capacity.  Damage encompasses mechanical cracking, material decay (due to 

         chemical or physical attack) or whatever phenomena influencing on the original capacity of 

         materials and structural members. 

          

         6. History.  History  is an essential dimension of the building  and must be considered and 

         integrated in the model. The following effects linked to history may have had influence on the 

         structural response and existing damage:  Construction process,  architectural alterations, 

         additions, destruction in occasion of conflicts (wars…), natural disasters (earthquake, floods, 

         fires…) and long-term decay or damage phenomena. History constitutes a source for knowledge. 

         In many occasions, the historical performance of the building can be engineered to obtain 

         conclusions on the structural performance and strength. For instance, the performance shown 

         during past earthquakes can be considered to improve the understanding on the seismic capacity. 

         The history of the building constitutes a unique experiment occurred in true scale of space and 

         time. In a way, knowledge of historical performance  makes up for the mentioned data 

         insufficiency. 

          

         2.  Desirable features of methods applied to historical structures 

         Because of the aforementioned challenges, attempts to model and simulate the response of a 

         historical structure should try to satisfy some basic requirements. Firstly, any modelling technique 

         should be able to adequately describe the geometry and morphology of the real construction, 

         including the structural form, internal composition, connections and support conditions. An 

         accurate description of the distribution of mass and external forces is essential for both gravity 

         and seismic analyses.   

         Secondly, constitutive equations should be adopted allowing an adequate description of the 

         essential mechanical and strength features of the different materials existing in the building.  It is 

         important to highlight that simple linear elastic analysis fails to simulate essential features of non-

         tension resisting materials such  as stone and masonry. More sophisticated, non-linear 

         constitutive equations will normally be necessary.  In turn, the use of such constitutive equations 

         will require the availability of non-linear properties to be obtained by means of different laboratory 

         or in-situ mechanical tests. 

         Actions (mechanical, physical, chemical...) are also to be modelled by means of mathematical 

         formulations describing their mechanical effect in terms for forces on the structure, imposed 

         movements or deformations, or possible variations of the material properties.  

         An accurate model of the structure should also afford the description of damage and alterations 

         existing in the structure, including cracks, disconnections, crushing, deformation and out-of-

         plumb,  and construction defects. Some damage types can be modelled indirectly as a 

         disconnection between elements or a local reduction of material properties. In order to 

         characterize the actual capacity in the present condition of a building, the analysis should be 

         carried out on the model accounting for its real damaged and deformed state. 

         As the analysis of historical structures will normally be oriented to identify needs for restoration 

         and strengthening, analysis methods should able to incorporate and model possible stabilization, 

         repair or strengthening measures. In some cases, these can be taken into account in an indirect 

         way by adequately modifying material properties, modifying the sectional dimensions or 

         configuration, or by adding forces to represent their mechanical effect.

## [p. 6]

6 

          

         The interaction of the structure with the soil is also to be taken into account except in cases it is 

         judged to be irrelevant. Taking it into account will often require the inclusion of a large portion of 

         foundation soil as part of the entire FEM model as done in the analysis of San Marcos Basilica by 

         Mola and Vitaliani (1995) or the modal analysis of a masonry tower by Fanelli (1993) (Figs. 2 and 

         3). 

          

          

          

                                              

                                                

         Fig. 2: The finite element model of the St. Mark’s Basilica: Top: global discretization; Bottom:  soil 

         foundation discretization including deformation (Mola and Vitaliani 1995).

## [p. 7]

7 

          

                                                     

         Fig.  3: Examples of graphical rendering for a FE mathematical model of a masonry tower: 

         discretized geometry, including the soil foundation, and first two vibration modal shapes (Fanelli, 

         1993). 

         Certain types of analyses, as in particular dynamic one, may require the inclusion of neighbouring 

         buildings into the model with an adequate description of existing connections. This is so because 

         of their possible effect on the modal shapes and overall dynamic response.  Modelling accurately 

         the dynamic response will often require to construct a global model incorporating all the distinct 

         parts of a complex structure as in the analysis of Reggio Emilia Cathedral (Casarin, 2006, Casarin 

         and Modena, 2008), of the Monastery of Jerónimos (Lourenço and Mourão, 2001) or of Mallorca 

         Cathedral (Roca et al., 2009) (Fig. 4-6). The connection between the different parts should be 

         modelled accurately by taking into account the real contact conditions, which requires a previous 

         detailed inspection and investigation. The agreement between numerical and experimental 

         vibration modes and frequencies may be considered as a way to validate the description of 

         connection among different parts in the structure. .  

          

                                                     

         Fig. 4: Different stages of the model (a) to (d) and successive boundary conditions variation 

         (Casarin, 2006). The surrounding buildings are taken into account by directly modelling their walls 

         or by simulating them with translational springs.

## [p. 8]

8 

          

                                        

         Fig. 5: Deformed meshes and maximum displacements (in grey scale) for seismic load acting 

         along the longitudinal direction of the building. Monastery of Jerónimos (Lourenço and Mourão,  

         2001). 

          

                                                    

          

         Fig. 6. Detailed modelling of Mallorca cathedral, in Spain, including the different parts of the 

         structure which can influence on the modal analysis (tower, façade, choir) and first modal shapes 

         (Roca et al., 2009). 

         Studies on different historical structures (Roca 2004, Roca et al., 2004) have shown that real 

         deformations are normally much larger (one or even two orders of magnitude) than those 

         predicted by conventional instantaneous calculations. This is due to the fact that these analysis 

         neglect history-related aspects  such as (1) deformations occurred during the  construction 

         process, as those due to the deflection of centerings and forms, and the deformation of structural 

         members during intermediate and incomplete configurations of the structure, (2) initial and 

         historical soil settlements, (3) architectural alterations, (4) the non-reversible effect of multiple 

         thermal and hygrometric cycles, and (4) long term damage of mechanical, physical or chemical 

         nature, among other phenomena.   

         A significant part of the damage and deformation today visible in ancient construction may have 

         been experienced during the construction process or at very early stages of the structure’s life.  

         Because of it, it is hardly possible to determine the amount of deformation mechanically 

         connected to the gravity forces or other possible actions. In any case, a good approach to the 

         prediction of deformation and, possibly, damage, can hardly be derived from a purely 

         instantaneous analysis which does not take into account, to some extent, the changes and

## [p. 9]

9 

          

         historical events or physical phenomena affecting the structure. Accurate studies should ideally 

         afford the simulation of the following aspects:  

         (1)  the subsequent historical stages experienced by the building (in particular, the construction 

           process) through a sequential analysis,  

         (2)  the actions occurring in historical periods, such as major earthquakes or the repeated effect 

           of minor earthquakes or thermal cycles, and  

         (3)  long-term damage processes (such as those related to long-term creep) developed across 

           the life of the construction.   

         As observed apropos of the study of the collapse of the Civic Tower of Pavia and Noto Cathedral 

         in Italy, (Papa and Taliercio, 2000, Binda, et al. 1992, 2001, 2003), the effect of creep under 

         constant stress, at the long term, may induce significant, cumulative damage in rock-like 

         materials. The investigation of specimens cut from the walls of the Pavia Tower after its collapse 

         allowed to Anzani et al. (2008) the formulation, for the first time on ancient masonry, of the 

         hypothesis of a collapse due to the long-term behaviour of the material. The identification of the 

         problem fostered some research effort to better characterize the phenomenon, and some models 

         have been already proposed for its description (Lourenço and Pina-Henriques, 2008, Taliercio 

         and Papa, 2008). 

         It must be noted, however, that a realistic simulation of historical actions or long-term damage 

         processes is still requiring additional experimental studies and numerical developments.  In fact, 

         limitations linked to the capacity of the computers and data available make it very difficult to 

         integrate the aforementioned capabilities in the analyses. A realistic modelling including both 

         structural history and time-dependent effects is, at the moment, still too demanding with regard 

         to the possibilities of conventional calculations approaches. However, these aspects may be 

         taken into account in an approximate way or may at least be considered to obtain a better 

         interpretation the results.   

         As an attempt to examine the influence of the architectural alterations experienced by the 

         structure of Tarazona Cathedral in Spain (Roca, 2001, Fig. 7), the analysis was independently 

         carried out on a series of structural configurations corresponding to different historical moments. 

         For the analysis of Mallorca cathedral, whose final condition is believed to have been very much 

         affected by a delicate construction process, a true sequential analysis was carried out involving 

         the superposition of two consecutive construction stages (Clemente,  2006, Fig. 8).  The 

         construction process was reconstructed thanks to a detailed research on historical documents.  

         The deformation and damage predicted by the sequential analysis was significantly larger than 

         those obtained by instantaneous analysis on the final structural configuration.

## [p. 10]

10 

                  

                                                                                                    

                                (a)                                (b)                              (c)                                  (d) 

                 Fig. 7. Analysis of Tarazona Cathedral for different historical configurations (Roca, 2001) by FEM 

                 isotropic damage model. (a) Distribution of tensile damage at the initial condition after construction 

                    th  th

                 (12  -13  c.); (b) Compression damage after overloading of lateral vaults during late Middle Age; 

                                      2                         th

                 (c) tensile stresses (N/m ) after “thinning” of piers (16  c.);  tensile damage during momentary 

                                                                 th

                 dismantling of flying arches for restoration purposes (20  c.). 

                    

                                                                                   

                   

                  

                 Fig. 8. Sequential analysis of Mallorca Cathedral taking into account the construction process 

                 (Clemente 2006) using a FEM isotropic damage  model.  Phases considered (left) and 

                 corresponding distribution of deformation and damage (right). 

                  

                 3. Review of classical methods 

                 It was Robert Hooke who discovered that the ideal shape of a masonry arch in equilibrium is that 

                 of the inverted catenary curve drawn by a chain subjected to the same weight distribution. At the 

                 end of a printed lecture on Helioscopes and some other instruments in 1676 he inserted the 

                 following problem: “The true mathematical and mechanical form of all manner of arches for 

                 building, with the true butment necessary to each of them. A problem which no architectonick 

                 writer hath ever yet attemted, much less performed”. He then provided the solution in the form of 

                 an anagram whose decipherment was only revealed after his death in 1705. The solution read: 

                 "Ut pendet continuum flexile, sic stabit contiguum rigidum inversum” - as hangs a flexible cable, 

                 so inverted, stand the touching pieces of an arch (Heyman, 1989). Meanwhile, the equation for 

                 the curve of a hanging flexible line or catenary had been already derived by David Gregory, who

## [p. 11]

11 

                   

                  by 1698 had independently reached and extended Hooke's assertion to the case of material 

                  arches with finite thickness.  According to Gregory, arches are stable when some catenary can 

                  be fitted within its thickness. 

                  The possibility of analysing masonry arches by the analogy between the equilibrium of 

                                                                                th      th 

                  compressed members with that of funicular models was used during 18  and 19 c., and even at 

                                  th

                  the beginning of 20  c., for the design and assessment of masonry bridges and buildings.  A well-

                  known example is the study of the dome of St. Peter in the Vatican by Poleni (1743), Fig. 9.  At 

                                  th

                  the beginning of 20  c., architect A. Gaudí used the same principle to design complex structures, 

                  such as the Church of Colònia Güell near Barcelona, by means of 3D hanging models (Fig. 10).  

                                                                               

                    Fig. 9. Poleni’s solution to describing the equilibrium of Saint Peter’s dome as the inverted 

                                             shape of a catenary (Poleni, 1743)  

                   

                   

                   

                   

                   

                   

                   

                   

                   

                   

                  Fig. 10. Gaudi’s hanging model used to design the church of Colònia Güell c. 1900 (Ràfols 1929).

## [p. 12]

12 

               

                              th

              In France, during the 18  c., La Hire, Couplet and Coulomb undertook the problem from a different 

              approach. Their understanding resulted from viewing the arch as a conjunction of rigid bodies 

              which could experience relative displacements. According to Couplet, the collapse occurs when 

              the arch develops enough hinges (or sections experiencing a relative rotation) as to become a 

              mechanism (Heyman, 1976). The first general theory on the stability of arches was published by 

              Coulomb in his 1773 essay. Coulomb developed a consistent and general theory providing the 

              mathematical base for the description of the different possible modes of collapse, taking into 

              account both relative rotations and sliding between parts. He also stated that the failure due to 

              sliding is rare and suggested to consider only overturning  (rotational) failures for practical 

              purposes. He proposed the use of a theory of “maxima and minima” (from our modern point of 

              view, and optimization method) to determine the position of the more unfavourable hinges or 

              sections of rupture.  

                                                                       th

              A further development arrived with the thrust line theory and graphic statics during 19  c. Graphic 

              statics supplied a practical method consistently based on the catenary principle. Graphic statics 

              was actually used for the assessment of a large amount of masonry bridges and large buildings 

                               th

              up to the beginning of 20  c. An example is given by Rubio’s analysis of the structure of Mallorca 

              Cathedral (Rubió, 1912,  Fig. 11).  Huerta (2001) provides a comprehensive review of the 

              application of the thrust line theory to the analysis of vaults and domes. 

               

                                                               

              Fig. 11. Rubió’s (1912) application of graphic statics to analyze the stability of Mallorca Cathedral 

              (detail).

## [p. 13]

13 

          

         4.  Modern theories to support classical approaches. Plastic analysis. 

         Heyman’s (1966) formulation for the plastic (or limit) analysis of masonry arches synthesizes all 

         the mentioned historical insights and provides a powerful and theoretically sound tool for the study 

         of this type of constructions. According to this formulation, the limit theorems of plasticity can be 

         applied to masonry structures provided the following conditions are verified: (1) The compression 

         strength of the material is infinite; (2) Sliding between parts is impossible; (3) The tensile strength 

         of masonry is null. These conditions enable the application of the well known limit theorems of 

         plasticity.  

         In particular, these conditions enable the following formulation of the lower-bound (or safe) 

         theorem: The structure is safe, meaning that the collapse will not occur, if a statically admissible 

         state of equilibrium can be found. This occurs when a thrust line can be determined, in equilibrium 

         with the external loads, which falls within the boundaries of the structure. The load applied is a 

         lower-bound of the actual ultimate load (causing failure).  The lower-bound theorem supports the 

         so-called static approach (or static limit analysis) for safety assessment of masonry structures.  

         According to the upper-bound theorem, If a kinematically admissible mechanism can be found, 

         for which the work developed by external forces is positive or zero, then the arch will collapse. In 

         other works, if a mechanism is assumed (by arbitrarily placing a sufficient number hinges), the 

         load which results from equating the work of the external forces to zero is an upper-bound of the 

         actual ultimate load. The application of the upper bound theorem leads to the so-called kinematic 

         approach (or kinematic limit analysis) for the study of masonry buildings. 

         A corollary of the safe theorem, the so-called uniqueness theorem, is also applicable: A limit 

         condition will be reached (i.e., the structure will be about to collapse) if a both statically and 

         kinematically admissible collapsing mechanism can be found. In other words, the collapsing 

         configuration will be reached if a thrust line can be found causing as many hinges as needed to 

         develop a mechanism. Hinges are caused by the thrust line becoming tangent to the boundaries. 

         When this occurs, the load is the true ultimate load, the mechanism is the true ultimate 

         mechanism, and the thrust line is the only possible one.  

         In spite of its ancient origin, limit analysis is regarded today as a powerful tool realistically 

         describing the safety and collapse of structures composed by blocks (including not only arches 

         and structures composed of arches, but also towers, façades and entire buildings). It must be 

         remarked, however, that it can hardly be used to describe the response and predict damage for 

         moderate or service load levels not leading to a limit condition. Strictly speaking, limit analysis 

         can only be used to assess the stability or safety of structures. 

         Limit analysis entails a very deep and conspicuous reality and should be always considered as a 

         complementary tool, or at least as a guiding intuition, when performing alternative computer 

         analyses. Experience shows that, no matter the level of sophistication of any computer method, 

         it will produce, at ultimate condition, results foreseeable by means of limit analysis.  

         Based on the observation of real seismic failure modes of historical and traditional buildings in 

         Italy, Giuffré (1990, 1995), see also Giuffrè and Carocci (1993) and Carocci (2001), proposed an 

         approach for the study  of the seismic  vulnerability of masonry buildings based on their 

         decomposition into rigid blocks (Figs. 12 and 13). The collapse mechanisms are then analyzed 

         by applying kinematic limit analysis. This approach is particularly interesting as a tool for seismic 

         analysis of buildings which do not conform to box behaviour because of lack of stiff floor slabs or 

         because of weaker partial collapses affecting the façade or inner walls.

## [p. 14]

14 

          

         More recently, Giuffré’s proposal has experienced renewed interest thanks to the possibility of 

         combining block analysis with the capacity spectrum method (Fajfar 1999, Lagormarsino et al., 

         2003, Lagomarsino, 2006) for the seismic assessment of masonry structures. The method is 

         applied to buildings, churches and towers (Fig. 14). The resulting verification methodology has 

         been adopted by the seismic Italian code OPCM 3274.   

          

         Research on the possibilities of classical limit analysis is still being carried out. Recently, improved 

         graphic oriented techniques for analysis of masonry arch and vault structures, based on the 

         combination of the static and kinematic approaches, have been presented by Block et al. (2006). 

         Limit analysis is currently exploited as a useful tool to analyze ancient structures (Ochsendorf, J, 

         2002, De Luca et al., 2004, Block, 2006). Roca et al. (2007) have produced a method for 

         graphically-oriented analysis of reinforced masonry structures based on the same principles. 

          

                                           

                                           

                                           

                                           

                                           

                                           

                                           

                                           

                                           

                                           

          

         Fig. 12. Failure modes for buildings with no ties (a) and with ties anchoring the façade to lateral 

         walls (Carocci, 2001). 

          

          

                                                    

                                                      

          

         Fig.13. Failure mechanisms for buildings embedded within urban texture (based on D’Ayala and 

         Speranza, 2002).

## [p. 15]

_(página sin capa de texto)_

## [p. 16]

16 

          

         wall subjected to seismic loads is given in Fig. 15, where the amount of horizontal forces resisted 

         is measured as a multiplier α over the gravity forces. 

          

                                             

         Fig. 15: Out of plane loaded wall, supported at one edge; (a) model; (b) FEM failure mechanism 

         (α = 0.210); (c) limit analysis failure mechanism (α= 0.216) (Orduña and Lourenço, 2005b). 

          

         Limit analysis formulation for blocky structures places some difficulties regarding the treatment of 

         the normality condition. Standard formulations adopt a simple frictional Coulomb law 

         characterized by a friction angle Φ at the contact interfaces. Applying the normality condition (or 

         associated flow rule) leads, in this case, to a fixed dilatancy (normal separation between blocks) 

         characterized by an angle ψ necessarily equal to Φ, where tanψ is the ratio between normal and 

         tangent deformation (Fig. 16). In reality, no physical condition leads to this value, real dilatancy 

         of masonry being variable and almost null in many cases. However, the limit theorems of 

         plasticity, previously enunciated, are only applicable when associated flow rules are adopted (i.e., 

         when the normality condition stands). Adopting a non-associated flow rule by assuming, for 

         instance, null dilantacy, leads to non-standard limit analysis for which the limit theorems are not 

         strictly applicable. Considering finite compression strength (for instance, by assuming a contact 

         region subjected to uniform yielding compression stresses) leads as well to non-standard limit 

         analysis. As shown by Orduña and Lourenço (2005a), looking to the safest solution by minimizing 

         the multipliers obtained by the kinematic approach (upper-bound theorem) may, for non associate 

         flow rules, cause severe underestimation of the collapse load and incorrect failure mechanisms. 

         Orduña and Lourenço (2005a) have overcome this problem by means of a load-path following 

         procedure in which equilibrium and yield conditions are first applied for only constant loads. Once 

         the constant loads have been applied, the variable ones are steadily increased. A solution for the 

         entire set of equations is obtained for a small compressive effective stress (i.e., a reduced 

         compression strength taking into account transverse cracking) at the interfaces and the load factor 

         is minimized. Then, solutions are computed for successively raising compressive effective 

         stresses until the assessed value is reached.   

          

         Gilbert et al. (2006), in turn, use a non-associative frictional joint model (a specially modified Mohr-

         Coulomb failure surface) which is continuously updated, within a iterative procedure, until a 

         converged solution is obtained. The procedure provides reasonable estimates of the ultimate 

         capacity for a wide range of problems, including entire masonry façades (Fig. 17).

## [p. 17]

17 

          

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

                                               

         Fig. 16. Associated flow rule (top) with μ=tanΦ=tanψ, and non-associated flow rule (below), with 

         null dilatancy (tan ψ=0). The yield criterion is represented as relationship between the normal (N) 

         and shear forces (V). The corresponding displacements are the normal (δn) and tangent (δs) 

         ones.   

          

          

          

                                                     

          

         Fig. 17. Failure modes for walls subjected to vertical and horizontal loading obtained by Gilbert et 

         al. (2006).

## [p. 18]

18 

          

         5.2 Limit analysis of domes, vaults and complex spatial structures 

         Recent proposals are exploring the potential of the lower-bound theorem (static approach) for the 

         analysis of vaulted and 3D spatial systems. A formulation for the analysis of curved shell masonry 

         members was presented by O’Dwyer (1999), consisting of the decomposition of the shell element 

         into a system of arches in equilibrium. By applying the safe theorem and maximizing the ultimate 

         load, via an optimization process, O’Dwyer establishes a procedure which allows the general 

         application of Heyman’s limit analysis to vaults and domes.  Block and Ochsendorf (2007) have 

         presented a Thrust-Network Analysis method for generating compression-only surfaces and 

         spatial systems based on a duality between geometry and in-plane forces in networks. The 

         method is applicable to the analysis of vaulted historical structures and for the design of new 

         vaulted ones. Lucchesi et al. (2007) have generalized the static approach for arches to the case 

         of masonry vaults through a maximum modulus eccentricities surface, a concept analogous to 

         the line of thrust in the case of arches.  

         Andreu et al. (2006, 2007) have developed a computer technique for the assessment of complex 

         masonry constructions, including 3D framed structures and shells, inspired on Gaudi’s hanging 

         models (Fig.18). Skeletal masonry constructions are modelled as 3D catenary nets composed of 

         numerous virtual strings subjected to arbitrary loading. Based on this description, limit analysis is 

         applied according to the static approach.  Cable net solutions complying with the limit theorems 

         of plasticity –in particular, the safe (or lower-bound) and the uniqueness theorems- are generated 

         by means of convenient optimization techniques.  

                                           

          

          

          

          

          

          

          

         Fig 18.  Examples of inverted multiple nets (top) and application to describe the equilibrium 

         condition of a tower of the façade of Barcelona Cathedral (Andreu et al., 2006).

## [p. 19]

19 

          

          6.  Elastic linear analysis.  Possibilities and limitations.  

         Linear elastic analysis is commonly used in the calculation of steel and reinforced concrete 

         structures. However, its application to masonry structures is, in principle, inadequate because it 

         does not take into account the non-tension response and other essential features of masonry 

         behaviour. It must be noted that, due to its very limited capacity in tension, masonry shows a 

         complex non-linear response even at low or moderate stress levels. Moreover, simple linear 

         elastic analysis cannot be used to simulate masonry strength responses, typically observed in 

         arches and vaults, characterized by the development of  partialized subsystems working in 

         compression. Attempts to use linear elastic analysis to dimension arches may result in very 

         conservative or inaccurate approaches. Linear elastic analysis is not useful, in particular, to 

         estimate the ultimate response of masonry structures and should not be used to conclude on their 

         strength and structural safety. 

         Notwithstanding, linear elastic analysis has been used, with partial success, as an auxiliary tool 

         assisting in the diagnosis of large masonry structures. Easy availability and reduced computer 

         costs have promoted its use, in spite of the mentioned limitations, before the development and 

         popularization of more powerful computer applications.  

         Some examples are the studies of San Marco in Venice (Mola and Vitaliani, 1995), Fig. 3, the 

         Metropolitan Cathedral of Mexico (Meli and Sánchez-Ramírez 1995), the Tower of Pisa (Macchi 

         et al., 1993), the Colosseum of Rome (Croci, 1995) (Fig.2) and the Church of the Güell Colony in 

         Barcelona, by Gonzalez et al. (1993), see also and Roca (1998), Fig. 19, among many other. The 

         case of Hagia Sophia has deserved much attention and has been analyzed by different authors 

         using similar modeling techniques (Mark et al, 1993a, 1993b, Croci et al, 1997, and others). In all 

         these cases, the limitations of the method were counterbalanced by the very large expertise and 

         deep insight of the analysts.   

         During the last years, non-linear analysis is becoming more popular thanks to larger software 

         availability and increasing computer capacity. However, linear analysis is always performed, prior 

         to the application of more sophisticated approaches, to allow a quick and first assessment of the 

         adequacy of the structural models regarding the definition of meshes, the values and distribution 

         of loads and reactions, and the likelihood of the overall results.  

         Meli and Peña (2004) have discussed the possibilities of elastic-linear models in providing 

         preliminary information for the seismic study of masonry churches and the possibility of using 

         information obtained from them for constructing more detailed models of critical parts to be then 

         studied separately with more complex analyses.  

          

         7.  Simplified modelling 

         7.1 Extensions of matrix calculation for linear members  

         The limitations of linear elastic analysis, on the one hand, and limit analysis, on the other hand, 

         can be partly overcome by means of simple generalizations of matrix calculation of frame 

         structures, extended with (1) Improved techniques for the description of complex geometries 

         (curved members with variable sections…) and (2) Improved description of the material (for 

         instance, including simple constitutive  equations yet affording the consideration of cracking in 

         tension and yielding / crushing in compression, yielding in shear).

## [p. 20]

20 

          

                                                 

         Fig. 16: Linear elastic analysis of the Crypt of the Güell Colony near Barcelona (Roca, 1998). 

         Regions subjected to tensile normal stresses are represented in red colour.  

          

         These tools are, in principle, only applicable to 2D or 3D systems composed of linear members 

         (namely, skeletal structures). However, there are some proposals to treat 2D members (vaults, 

         walls) as equivalent systems composed of beams.  

         In fact, the application of conventional frame discretization yields inaccurate results when dealing 

         with shear wall systems (Karantoni and Fardis, 1992). However, these results can be improved 

         through the definition of a set of special devices to represent more realistically the shear 

         deformation of the walls. Among some different proposals, Kwan's (1991) technique, in which the 

         shear deformation of the walls is transferred to  rigid  arms connecting wall panels or walls with 

         lintels, has shown to be very accurate for both  solid or hollow walls and façades.   

         Molins and Roca (1998) developed a method for the analysis of masonry skeletal structures as 

         an extension of conventional matrix calculation to systems composed of curved members with 

         variable cross-section. The method includes a set of partial models for the description of the non-

         linear response of masonry taking into account cracking in tension and yielding or crushing in 

         compression. Roca et al. (2005) extended the method to analyse 3D systems including masonry 

         load bearing walls using Kwan’s proposal for the modelling of wall systems as equivalent frames. 

         The method has been successfully used in the assessment of façades and entire buildings. 

          

         7.2 Use of rigid and deformable macroelements 

         Important research efforts have been devoted to the development of computational approaches 

         based on rigid and deformable macroelements. Each macroelement models an entire wall or 

         masonry panel, reducing drastically the number of degrees of freedom of the structure. Brencich, 

         Gambarotta and Lagomarsino (1998, Fig. 20) use two nodes macroelements taking into account 

         the overturning, damage and frictional shear mechanisms experimentally observed in masonry 

         panels. The overall response of buildings to horizontal forces superimposed to the vertical loads 

         is obtained by assembling shear walls and flexible floor diaphragms. The former are made up of 

         both macroelements, representative of piers and spandrels, and rigid elements, representing the 

         undamaged parts of the walls.

## [p. 21]

21 

          

          

         More recent developments, as those due to Casolo and Peña (2007) and Chen et al. (2008), 

         show the permanent interest of this type of simplified approaches and their ability to combine 

         satisfactory accuracy with computer efficiency.  

          

          

                                                

         Fig. 20. Analysis with macro-blocks of a façade wall tested by Calvi and Magenes (1994). Damage 

         distribution under monotonic loading (Brencich, Gambarotta and Lagomarsino, 1998) at peak load 

         (A) and at the end of the monotonic load history (B). 

         Casolo and Peña (2007) have developed a specific rigid element approach for the in-plane 

         dynamic analysis of masonry walls.  A rigid body spring model (RBSM) has been adopted 

         consisting of a collection of plane quadrilateral rigid elements connected to each other by two 

         normal springs and one shear spring at each side.  Specific separate hysteretic laws are assigned 

         to the axial and shear deformation between elements.  A Coulomb-like law is adopted to relate 

         the strength of the shear springs to the vertical axial loading. The satisfactory performance of the 

         approach has been proven by comparison with available experimental and numerical results on 

         pier walls and façades. The technique has been also successfully applied to the study of a large 

         real masonry construction, namely the Maniace Castle in Syracuse (Casolo and Sanjust, 2009). 

          

         8.  FEM based approaches. Macro-modelling 

         The finite element method offers a widespread variety of possibilities concerning the description 

         of the masonry structures within the frame of detailed non-linear analysis. An example of a 

         pioneering application is found in Mark’s et al. (1993) analysis of Hagia Sophia allowing different 

         portions of the structure to weaken at different levels of tension.  

         Most of modern possibilities based on FEM fall within two main approaches referred to as macro-

         modelling and micro-modelling.

## [p. 22]

22 

          

         Macro-modelling is probably the most popular and common approach due to its lesser calculation 

         demands. In practice-oriented analyses on large structural members or full structures, a detailed 

         description of the interaction between units and mortar may not be necessary. In these cases, 

         macro-modelling, which does not make any distinction between units and joints, may offer an 

         adequate approach to the characterization of the structural response. The macro-modelling 

         strategy regards the material as a fictitious homogeneous orthotropic continuum.  

         An appropriate relationship is established between average masonry strains and average 

         masonry stresses. A complete macro-model must account for different tensile and compressive 

         strengths along the material axes as well as different inelastic properties along each material axis. 

         The continuum parameters must be determined by means of tests on specimens of sufficiently 

         large size subjected to homogeneous states of stress. As an alternative to difficult experimental 

         tests, it is possible to assess experimentally the individual components (or simple wallets and 

         cores, see Benedetti et al. 2008) and consider the obtained data as input parameters of a 

         numerical homogenization technique. Compared to more detailed approaches affording the 

         description of discontinuities, macro-modelling shows significant practical advantages. In 

         particular, FE meshes are simpler since they do not have to accurately describe the internal 

         structure of masonry and the finite elements can have dimensions greater than the single brick 

         units. This type of modelling is most valuable when a compromise between accuracy and 

         efficiency is needed. 

         The macro-models, also termed Continuum Mechanics finite element models, can be related to 

         plasticity or damage constitutive laws. An example of the former approach is the work of Lourenço 

         (1996) and Lourenço et al. (1998) which proposed a non-linear constitutive model for in-plane 

         loaded walls based on the plasticity theory, for which the material admissible field is bounded by 

         a Hill-type yield criterion for compression and a Rankine-type yield criterion for tension (Fig. 21). 

                                                     

         Fig. 21. Analysis of a shear wall with the plasticity model of Lourenço et al. (1998): deformed 

         mesh (a) and cracks (b). 

          

         In the case of Continuum Damage finite element models, isotropic criteria have been usually 

         preferred because of their mathematical simplicity and the need for only few material parameters. 

         However, a number of orthotropic models have been also proposed. Papa’s (1996) orthotropic 

         model consists of a unilateral damage model for masonry including a homogenization technique 

         to keep into account the texture of brick and mortar. Berto et al. (2002) developed a specific 

         damage model for orthotropic brittle materials with different elastic and inelastic properties along 

         the two material directions. The basic assumption of the model is the acceptance of the natural 

         axes of the masonry (i.e. the bed joints and the head joints directions) also as principal axes of 

         the damage (Fig. 22).

## [p. 23]

_(página sin capa de texto)_

## [p. 24]

24 

          

                                             

         Fig. 23. Analysis of Küçük Ayasofya Mosque in Istanbul by a damage mechanics –based macro-

         model. Distribution of tensile damage parameter (in chromatic scale) for the structure subjected 

         to dead loading (Roca et al. 2004). 

          

                                          

         Fig. 24. Seismic analysis of Mallorca Cathedral. Smeared damage approach (a) versus localized 

         damage approach (b), for an earthquake of 475 years of return period (Clemente et al., 2006). 

         Both diagrams represent the tensile damage scalar parameter in chromatic scale.

## [p. 25]

25 

          

         A drawback of the macro-modelling approach lays in its description of damage as a smeared 

         property spreading over a large volume of the structure. In real unreinforced masonry structures, 

         damage appears normally localized in isolate large cracks or similar concentrated lesions. A 

         smeared modelling of damage provides a rather unrealistic description of damage and may result 

         in predictions either inaccurate or difficult to associate with real observations. 

         An interesting enhancement to smeared damage representation  was  recently  proposed by 

         Clemente et al. (2006). The method is based on the so-called smeared-crack scalar damage 

         model, modified in such a way that it can reproduce localized individual (discrete) cracks. This is 

         achieved by means of a local crack-tracking algorithm. The crack tracking model enables the 

         simulation of more realistic damage distributions than the original smeared-crack model. The 

         localized cracks predicted by the crack tracking model behave, in consistency with limit analysis, 

         as a set o hinges developing gradually and finally leading to a full collapsing mechanism. The 

         model has been used to analyze the response of the structure of Mallorca Cathedral under gravity 

         and seismic forces (Fig. 24).  More recently, Clemente’s et al. (2006) isotropic damage has been 

         modified to account for masonry’s orthotropy by Pelà et al. (2008, see also Pelà 2009). 

         Very few attempts to combine non-linear constitutive equations with solid 3D element meshes 

         have been formulated. Oñate et al., (1995), see also Hanganu (1997), proposed a 3D continuum 

         damage model for masonry and concrete under physical and environmental effects and applied 

         it to the study of the Domes of the San Marco's Basilica in Venice. The model was later used to 

         study Barcelona Cathedral (Roca et al. 1998).  

          

         9. FEM based approaches. Discontinuous models 

         Macro-models encounter a significant limitation in their inability to simulate strong discontinuities 

         between different blocks or parts of the masonry construction. Such  discontinuities, 

         corresponding either to physical joints or individual cracks formed later in the structure, may 

         experience phenomena such as block separation, rotation or frictional sliding which are not easily 

         describable by means of a FEM approach strictly based on continuum mechanics.  

         A possible way of overcoming these limitations consists of the inclusion within the FEM mesh of 

         joint interface-elements to model the response of discontinuities. A pioneering application of this 

         possibility is found in Mark’s et al. (1993a) study of the buttresses of Hagia Sophia in Istambul by 

         means of a model combining large blocks with interface elements allowing the sliding along the 

         large blocks shaping the structure. 

         A more sophisticated set of discontinuous models was used by Pegon et al. (1995, 2001) to study 

         the seismic response of the cloisters of the São Vicente de Fora Monastery in Lisbon. A full-scale 

         model of part of the cloisters was built in laboratory and was subjected to intensive 

         experimentation  to, among other purposes,  validate  the models. The models included joint 

         models to simulate the block-to-block and block-to-masonry interfaces. Elastic-perfectly-plastic 

         and material softening joint models were used. The plastic range was defined by means of a 

         Mohr-Coulom law characterized by a friction angle and acohesion. However, the softening model 

         allowed the initial friction angle to decrease towards a residual value, whereas the cohesion 

         remained constant. The study included a combination of 2D analyses involving the entire façade 

         with more detailed 3D analysis on selected parts of the structure (Fig. 25). The material between 

         the joints (stone or brick masonry) was described as either linear elastic or non-linear plastic 

         homogeneous material.

## [p. 26]

26 

          

                                                     

         Fig. 25. 3D failure mechanism of part of the cloister of São Vicente de Fora Monastery in Lisbon 

         as obtained by Pegon et al. (2001). 

          

         9.  FEM based approaches. Micro-modelling 

         In the micro-modelling strategy, the different components, namely the units, mortar and the 

         unit/mortar interface are distinctly described. The so-called detailed micro-models describe the 

         units and the mortar at joints using continuum finite elements, whereas the unit-mortar interface 

         is represented by discontinuous elements accounting for potential crack or slip planes (Fig. 26). 

         Detailed micro-modelling is probably the more accurate tool available to simulate the real 

         behaviour of masonry. It is particularly adequate to describe the local response of the material. 

         Elastic and inelastic properties of both unit and mortar can be  realistically taken into account.  

         The detailed macro-modelling strategy leads to very accurate results, but requires an intensive 

         computational effort. This drawback is partially overcome by the simplified micro-models (Lotfi 

         and Shing, 1994; Tzamtzis, 1994; Lourenço and Rots, 1997, Fig. 27; Gambarotta and 

         Lagomarsino, 1997,  Fig. 28; Sutcliffe et al.,  2001), where expanded units,  represented by 

         continuum elements, are used to model both units and mortar material, while the behaviour of the 

         mortar joints and unit-mortar interfaces is lumped to  the  discontinuous elements (Fig.  26). 

         Masonry is thus considered as a set of elastic blocks bonded by potential fracture/slip lines at the 

         joints.   

         The micro-modelling approaches are suitable for small structural elements with particular interest 

         in strongly heterogeneous states of stress and strain. The primary aim is to closely represent 

         masonry based on the knowledge of the properties of each constituent and the interface. The 

         necessary experimental data must be obtained from laboratory tests on the constituents and small 

         masonry samples. Nevertheless, the high level of refinement required means an intensive 

         computational effort (i.e. great number of degrees of freedom of the numerical model), which limits 

         micro-models applicability to the analysis of small elements (as laboratory specimens) or small 

         structural details.

## [p. 27]

27 

          

                                                

         Fig.  26.  Modelling strategies for masonry structures (Lourenço, 1996): masonry sample (a); 

         detailed (b) and simplified (c) micro-modelling; macro-modelling (d). 

          

              

              

          

          

          

              

          

                                                  

         Fig.  27.  Micro-modelling of masonry shear walls (Lourenço, 1996). Top: Load-displacement 

         diagram. Bottom: Results of the analysis at a lateral displacement of 2.0 mm: (a) deformed mesh; 

         (b) damange.

## [p. 28]

28 

          

                                                 

         Fig.  28. Micro-modelling of masonry, from Gambarotta and Lagomarsino (1997). 

          

         10.  Homogenization 

         Midway between micro-modelling  and macro-modelling stands the  so-called  homogenized 

         modelling. If the structure is composed by a finite repetition of an elementary cell, masonry is 

         seen as a continuum whose constitutive relations are derived from the characteristics of its 

         individual components, namely blocks and mortar, and from the geometry of the elementary cell. 

         Most of the methods of homogenization simplify the geometry of the basic unit with a 2 step 

         introduction of vertical and horizontal joints and thus without taking into account the regular offset 

         of vertical mortar joints. However, this kind of approach results in significant errors when applied 

         to non-linear analysis.  

         Micromechanical homogenization, derived independently by van der Pluijm (1999), Lopez et al. 

         (1999) and Zucchini and Lourenço (2002), is based on the detailed finite element analysis of the 

         elementary cell and overcomes the approximations introduced by the 2 steps simplified method. 

         Recent advances in terms of sophisticated analysis homogenization tools are discussed in 

         Lourenço et al. (2007) and include the polynomial stress field expansion approach of Milani et al. 

         (2006a) and the mesoscopic approach of Massart et al. (2004), Calderini and Lagomarsino 

         (2006), and Shieh-Beygia and Pietruszczak (2008).   

         A micro-mechanical model for the homogenized limit analysis of in-plane loaded masonry has 

         been proposed by Milani et al. (2006a, 2006b, 2006c, 2007). It is developed with the aim to obtain 

         the homogenised failure surfaces for masonry. The strength domains are implemented in finite 

         element limit analysis codes and numerically treated both with a lower and an upper bound 

         approach  (Fig. 29). The main advantages of this method, compared with classical micro-

         modelling, are the following: (1) The finite element mesh does not have to reproduce the exact 

         pattern of the masonry units nor it has to be so fine. The structure can be meshed automatically. 

         (2) Once the homogeneous properties have been calculated from the micro-mechanical model, 

         standard finite element method can be used to perform the analysis avoiding the complications 

         introduced by elements interfaces.  

         The micro-mechanical approach has been successfully applied to both linear and non-linear 

         problems. In a first step, Zucchini and Lourenço (2002) introduced homogenization in the elastic 

         field by deriving the mechanical properties of masonry from a suitable micro-mechanical model 

         taking into account the staggered alignment of the units. The homogenisation model has been 

         subsequently extended to non-linear problems in the case of a masonry cell failure under tensile 

         loading parallel to the bed joint, Zucchini and Lourenço (2004), or under compressive loading

## [p. 29]

29 

          

         perpendicular to the bed joint, Zucchini and Lourenço (2007). These results are accomplished by 

         coupling the elastic micro-mechanical model with a damage model in tension and a plasticity 

         model in compression. To extend the model to mixed loading conditions Zucchini and Lourenço 

         (2009) used a full periodic cell with an antisymmetric deformation mechanism. The internal 

         structure of the cell is represented by five different components, namely units, two antisymmetric 

         bed joints, head joints and cross joints 

          

                                                  

         Fig.29.  3D homogenized limit analysis of  a masonry building (Milani et al. 2007). 

          

         11 Non-linear FEM analysis of vaulted structures 

         Few non-linear developments have been produced aiming to the analysis of vaulted structures. 

         Domes and vaults pose significant difficulties due to their curved, two-dimensional and spatial 

         character. In fact, most of the applications for non-linear analysis of masonry structures so far 

         mentioned are oriented to two-dimensional planar problems.   

         A pioneering work is found in the studies by Oñate et al. (1995) of the domes of San Marco 

         Basilica in Venice. The set of vaults was modelled by means of a continuum damage model for 

         masonry and concrete under mechanical and other (physical, chemical, biological) deterioration 

         effects.  The analysis attained a characterization of the safety condition of the system of vaults 

         (Fig. 30). 

         Croci et al. (1998a) carried out a finite element analysis of the Cathedral of Sta. María, in Vitoria, 

         Spain. The analysis, applied to the main transverse sections of the building and to the nave vaults, 

         followed an incremental strategy to account for cracking due to tension or shear stresses, as well 

         as the equilibrium second-order effects. Similar analyses were also used for the study of the

## [p. 30]

30 

          

         collapse of Beauvais Cathedral (Croci et al., 1998b) and the  effects of the earthquake of 

         September 1997 on the Basilica of Assisi (Croci, 1998). 

         Barthel (1993) elaborated very detailed finite element models to analyze Gothic cross-vaults.  The 

         models were used in combination with partial constitutive models enabling the simulation of 

         masonry cracking as well as sliding between arch ring joints.  

         Cauvin and Stagnitto (1993, 1995) carried out studies on Gothic cross vaults using both limit 

         analysis and FEM non-linear analysis. Their method was successfully applied to the study of the 

         central nave of Reims Cathedral. 

         Lourenço (1997) proposed a formulation for the study of masonry spatial and curved shells. To 

         our knowledge, it is the only one based on the micro-modelling technique. It includes constitutive 

         equations, stemming from plasticity, to simulate the response of the material in combination with 

         joint elements to describe the sliding of blocks. 

          

          

                                               

          

         Fig. 30. Study of Saint Marco’s domes in Venice by a continuum damage model (Oñate et 

         al.,1995).  

          

         12. Discrete element method 

         The Discrete element method (DEM) is characterized by the modeling of the material as an 

         assemblage of distinct blocks interacting along the boundaries. According to its pioneer 

         proposers, Cundall and Hart (1971), the name “discrete element” applies to a computer approach 

         only if (1) it allows finite displacements and rotations of discrete bodies, including the complete 

         detachment and (2) it can recognize new contacts between blocks automatically as the calculation 

         progresses.

## [p. 31]

31 

          

         The formulation, initially oriented to  the study of jointed rock, was later extended to other 

         engineering applications also requiring a detailed study of contact between blocks or particles, 

         such as soils and other granular materials (Ghaboussi J., Barbosa R., 1990). Finally, it has also 

         been applied to the modeling of masonry structures (Pagnoni, 1994; Lemos, 1998; Sincraian, 

         2001).  The common idea in the different applications of the discrete element method to masonry 

         is the idealization of the material as a discontinuum where joints are modeled as contact surfaces 

         between different blocks. This approach affords the modeling of various sources of non linear 

         beahaviour, including large displacements, and suits the study of failures in both the quasi static 

         and dynamic ranges. 

         Distinct element methods, discrete-finite elements and discontinuous deformation analysis are 

         different formulations of the discrete element method with important applications to masonry 

         structures.  

         Distinct element methods are direct derivations of the first work by Cundall and Hart. They involve 

         soft contact formulations where a normal interpenetration is needed to recognize contact between 

         two different bodies. The main features of these methods are: (1) No restriction of block shapes 

         and no limitation to the magnitudes of translational and rotational displacements. The 

         approximation that all the deformations occur at the surfaces of blocks is made. It is also assumed 

         that forces arise only at contacts between a corner and an edge. (2) Forces arise due to 

         deformation. A change in displacement results in a change in force which is added to the existing 

         force stored for the contact. (3) Accelerations are computed from the forces and moments for 

         each block. The accelerations are further integrated into velocity and displacements.  (4) Contact 

         updating is performed when the sum of the displacements of all of the elements has exceeded a 

         certain value. To increase the efficiency, only blocks within a certain distance range are checked 

         for new contacts.   

         Discrete-finite element methods recollect different attempts of combining FEM with multi-body 

         dynamics. Munjiza et al. (1995) developed a method for the simulation of fracturing problems 

         considering deformable blocks that may split and separate during the analysis. Mamaghani et al. 

         (1999) used a fixed contact system with a small deformation framework and finite deformations 

         concentrated in contact elements. Contacts, discontinuities and interfaces were considered as 

         bands with a finite thickness. The contact element was a two-nodded element having normal and 

         shear stiffnesses. The method was applied to the stability analysis of different masonry structures. 

         The failure mode of a masonry arch is shown in Fig. 31.

## [p. 32]

32 

          

          

                                         

                                         

                                         

                                         

                                         

                                         

                                         

                            Initial configuration                           Iteration no. 24 

                                           

                                           

                                           

                                           

                                           

                                           

                            Iteration no. 27                                 Iteration no. 30 

          

         Fig. 31. Failure mode of a masonry arch (Mamaghani et al., 1999). 

                

         The discontinuous derformation analysis (DDA) is a 2D method developed by Shi and Goodman 

         (1988) for rock engineering analysis subsequently applied to masonry (Ma et al. 1996). Blocks 

         are considered deformable but with a uniform strain and stress distribution. Contact is considered 

         rigid and no interpenetration is permitted. This condition is enforced numerically by an iterative 

         procedure at each time step.  

         The natural field of application of DEMs is composed by structures formed by regurarly shaped 

         masonry or stone blocks. Rocking motion of stone blocks (Peña et al. 2007), static and dynamic 

         analysis of load bearing walls (Pagnoni 1994,    Baggio and Trovalusci 1995, Schlegel and 

         Rautenstrauch 2004), stone bridges (Lemos 1995, Bicanic et al 2001), columns and architrave 

         (Papastamatiou and Psycharis 1993, Psycharis et al 2003, Fig. 33), arch and pillar (Pagnoni 1994, 

         Pagnoni and Vanzi 1995, Lemos 1998) are typical examples of DEM analysis. The analysis of 

         complex structures is still a controversial topic in DEM. Computational viability of analysis may 

         limit severily the number of block elements that can be included in a model. Models prepared to

## [p. 33]

33 

          

         simulate the response of real structures may result in too coarse or unrealistic discretizations or 

         2D, and specially, 3D real masonry structures. 

          

                                             

         Fig.  32.    Final position of the column-architrave model of the Parthenon Pronaos, without 

         reinforcement, for a simulated earthquake  (Psycharis et al., 2003). 

          

         13. Conclusions   

         In spite of the important advances experienced by structural analysis methods, the study of 

         masonry historical structures is still a challenging activity due to the  significant difficulties 

         encountered in the  description of their complex geometry, materials, morphology (member 

         composition and connections), and present condition, including damage and alterations. In 

         particular, the modelling of the mechanical behaviour of masonry is very demanding due to its 

         fragile nature in tension and composite character at the macro-scale. 

         A wide set of possibilities have been developed to describe masonry structures to different levels 

         of accuracy, from rough (but useful) engineering approaches to very detailed modelling taking 

         into account the distinct response of the individual components. A very significant effort is 

         undertaken at present to produce homogeneization criteria allowing a better interconnection 

         between the micro- and macro- analysis levels.   

         Detailed methods, such as micro-models, are still requiring high computer effort and, in practice, 

         can only be used to analyze small individual members such as solid or hollow walls. Moreover, 

         the  sophisticated  methods often require complex material properties which can only be 

         determined through costly and sophisticated laboratory experiments. In the case of the study of 

         real buildings, such properties are not normally available and need to be indirectly estimated 

         based on more common and available evidence. However, inadequate assumptions on these

## [p. 34]

34 

          

         properties may compromise the real gain in accuracy provided by sophisticate method and even 

         lead to inadequate results.  

         With further developments in computer technology and numerical methods, the analysis of entire 

         complex historical structures (including for instance, Gothic cathedrals) using very accurate 

         approaches, may become possible in the near future. Further developments will make very 

         demanding analyses, such as the non-linear time-domain dynamic one, possible even if used in 

         combination with complex structural and material models. However, many of the difficulties 

         mentioned, as those related to the adequate survey and description of the structure, including 

         material features and damage, will still compromise the accuracy and realism of the numerical 

         predictions. In this context, the judgment of the analyst is essential in order to conclude on the 

         acceptability of the results.  

         Sufficient validation or calibration of numerical models, based on the comparison with empirical 

         information, will be always necessary to grant the reliability of the numerical models and their 

         capacity to predict on the structural response and safety. In the case of historical structures, this 

         empirical information can be obtained from historical investigation on the past performance, 

         inspection and monitoring (Icomos/Iscarsah Comittee, 2005). In the study of a historical structure, 

         structural analysis is a key activity to be developed in combination with other complementary, but 

         also important activities oriented to both gathering the input information and allowing later 

         calibration or validation of results.   

          

         Acknowledgements 

         Part of the studies presented here were developed within the research projects SEDUREC and 

         BIA2004-05552, funded by DGE of the Spanish Ministry of Science and Technology, whose 

         assistance is gratefully acknowledged.   

          

         REFERENCES 

        Ali, S.S. and Page, A.W.  (1988). Finite element model for masonry subjected to concentrated loads, 

        Journal of  Structural Engineering   ASCE,  114, (8), 1761-1784.  

        Andreu, A., Gil, L., Roca, P. (2006). Limit analysis of masonry constructions by 3D funicular 

        modeling.  Structural Analysis of Historical Constructions, MacMillan, New Deli, 1135-1142.  

        Andreu, A., Gil, L., Roca, P. (2007). Computational analysis of masonry structures with a funicular 

        model. Journal of Engineering Mechanics ASCE, 133 (4) 473-480. 

        Anzani, A., Binda, L., Mirabella-Roberti, G. (2008) Experimental researches into long-term behavior 

        of historical masonry. Learning from failure. Long term behaviour of heavy masonry structures. 

        Binda, L. (Ed). WIT Press, Southampton 

        Baggio, C., and Trovalusci, P. (1995). Stone assemblies under in-plane actions – comparison 

        between nonlinear discrete approaches. Computer methods in structural masonry, 3, 184-193. 

        Baggio, C., Trovalusci, P. (1998). Limit analysis for no-tension and frictional three-dimensional 

        discrete systems.  Mech. Struct.& Mach., 26(3), 287-304.

## [p. 35]

35 

          

        Barthel, R. (1993). Rissbildung in gemauerten Kreutzgewölben. Structural Preservation of the 

        Architectural Heritage, IABSE, Zürich, Switzerland. 

        Benedetti, A., Pelà, L. and Aprile, A. (2008). Masonry Property Determination via Splitting Tests on 

        Cores with a Rotated Mortar Layer. Proceedings of the 8th international seminar on structural 

        masonry. ISSM 08. Istanbul, Turkey. 5-7 novembre 2008, 647 – 655. 

        Berto L., Saetta A., Scotta R., Vitaliani R. (2002). An orthotropic damage model for masonry 

        structures. International Journal for Numerical Methods in Engineering. 55, 127-157. 

        Bicanic, N., Ponniah, D., and Robinson, J. (2001). Discontinuous deformation analysis of masonry 

        bridges. Computational Modelling of Masonry, 177-196. 

        Binda L., Gatti G., Mangano G., Poggi C., Sacchi Landriani G. (1992). The collapse of the Civic 

        Tower of Pavia: a survey of the materials and structure, Masonry International, vol. 6, n.1, 11-20. 

        Binda L., Modena C., Baronio G., Abbaneo S. (1997) Repair and investigation techniques for stone 

        masonry walls, in Construction and Building Materials, Vol. 11, N.3, 133-142. 

        Binda L., Saisi A., Messina S., Tringali S. (2001). Mechanical Damage Due to Long Term Behaviour 

        of Multiple Leaf Pillars in Sicilian Churches, III Int. Seminar: Historical Constructions 2001. 

        Possibilities of Numerical and Experimental Techniques, Guimaraes, Portugal, 707-718. 

        Binda L., Anzani A., Saisi A. (2003). Failure Due to Long Term Behaviour of Heavy Structures: the 

        Pavia Civic Tower and the Noto Cathedral, 8th Int. Conf. on STREMAH 2003, Struct. Studies 

        Repairs and Maintenance of Heritage Architecture, 7-9/5/2003, Halkidiki (Greece), 99-108. 

        Block, P. (2005). Equilibrium Systems. Studies in masonry structure. M.S. dissertation, Department 

        of Architecture, Massachusetts Institute of Technology. 

        Block, P., Ciblac, T., Ochsendorf, J. A. (2006) Real-Time Limit Analysis of Vaulted Masonry 

        Buildings. Computers and Structures 84 (2006) 1841–1852 

        Block, P., Ochserdorf, J. (2007) Thrust network analysis: a new methodology for three-dimensional 

        equilibrium. Journal of the International Associatio ofr Shell and Spatial Structures IASS, 48 (3), 

        155. 

        Brencich A., Gambarotta L., Lagomarsino S., (1998). A macroelement approach to the three-

        dimensional seismic analysis of masonry buildings. Proc. of the XI European Conf. on Earthquake 

        Engineering, Paris, A.A. Balkema (Abstract Volume & CD-ROM),  602. 

        Calderini, C., Lagomarsino, S. (2006). A micromechanical inelastic model for historical masonry. 

        Journal of Earthquake Engineering 10 (4), 453-479. 

        Calvi, G. M,  Magenes M. (1994) , Experimental research on response of URM building system in 

        Proc. of  US-Italy workshop on guidelines for seismic evaluation and rehabilitation of unreinforced 

        masonry buildings, State University of New York at Bufalo, Pavía, NCEER-94-0021, 3-41/57 

        Casarin, F. (2006). Structural Assessment and Seismic Vulnerability Analysis of a Complex 

        Historical Building. PhD Thesis, Università degli Studi di Padova. 

        Casarin, C., Modena, C. (2008) Seismic assessment of complex historical buildings: Application to 

        Reggio Emilia Cathedral, Italy. Journal of Architectural Heritage, 2 (3), 304-327.   

        Carocci, C. F. (2001) Guidelines for the safety and preservation of historical centres in seismic 

        areas. Historical Constructions, University of Minhi, Guimaraes, 145-165.

## [p. 36]

36 

          

        Casapulla C, D’Ayala  (2001) D. Lower bound approach to the limit analysis of 3D vaulted block 

        masonry structures. In: Proceedings of the 5th international symposium on computer methods in 

        structural masonry, STRUMAS V. Rome; 2001. p. 28–36. 

        Casolo, S., Sanjust, C. A. (2009) Seismic analysis and strengthening design of a masonry 

        monument by a rigid  body spring model: The “Maniace Castle” of Syracussa.   Engineering 

        Structures 31 (2009) 1447-1459 

        Casolo, S., Peña, F. (2007) Rigid element model for in-plane dynamics of masonry walls 

        considering hysteretic behaviour and damage. Earthquake engineering and structural dynamics. 

        36, 1029–1048 

        Cauvin, A., Stagnitto, G. (1993). Problems concerning strength assessment and repair of Historical 

        Vaulted Structures. Public Assembly Structures from Antiquity to the Present, IASS, Istanbul, 

        Turkey. 

        Cauvin, A., Stagnitto, G. (1995). Criteria of design and methods of structural analysis of Gothic 

        ribbed vaults using traditional and computer methods. Spatial Structures: Heritage, Present and 

        Future, SGE Editoriali, Padova, Italy. 

        Chen, S. Y., Moon, F. L., T. Yi, T. (2008) A macroelement for the nonlinear analysis of in-plane 

        unreinforced masonry piers. Engineering Structures 30, 2242–2252 

        Chiarugi, A., Fanelli, A., Giuseppetti, G. (1993) Diagnosis and strengthening of the Brunelleschi 

        Dome. IABSE Symposium 1993, IABSE, Zürich.  

        Clemente, R. (2006) Structural analysis of historical buildings by localized cracking models (in 

        Spanish). Ph. D. dissertation, Universitat Politècnica de Catalunya, Barcelona, Spain. 

        Clemente, R., Roca, P. and Cervera M. (2006). Damage  Model with Crack Localization – 

        Application to Historical Buildings: Structural Analysis of Historical Constructions, New Delhi, 1125-

        1135. 

        Coulomb, C. A.  (1773)  Essai sur une application des regles des maximis et minimis à quelques 

        problémes de statique relativs a l’arquitecture. Mémoires de Mathematique et de Physique 

        présentés à l’Académie Royal des Sciences per Divers Savants et lus dans ses Assemblées, 1, 

        París, p343-382. 

        Croci, G., Viscovik, A. (1993). Causes of failures of Colosseum over the centuries and evaluation 

        of the safety levels. Public Assembly Structures. From Antiquity to the Present.  IASS-Mimar Sinan 

        University, Istanbul, Turkey, 29-52. 

        Croci, G. (1995). The Colosseum: Safety Evaluation and Preliminary Criteria of Intervention. 

        Structural Analysis of Historical Constructions, Barcelona. 

        Croci, C., Cerone, M., Viskovic, A. (1997). Analysis from a historical and structural point of view of 

        the domes of Pantheon, Hagia Sophia and St. Peter. Studies in ancient structures. YTU Faculty of 

        Architecture Publication, Istanbul, Turkey 

        Croci, G. (1998). The Basilica of St. Francis of Assisi after the September 1997 Earthquake. 

        Structural Engineering International, Vol. 8, No. 1.  

        Croci, G., Carluccio, G., Viskovic, A. (1998a). Análisis estructural de la Catedral de Santa María 

        Vieja de Vitoria. Primer Congreso Europeo sobre Catedrales Góticas, Diputación Foral de Alava, 

        Vitoria, Spain.

## [p. 37]

37 

          

        Croci, G., Taupin, J. L., Viskovic, A. (1998b). Análisis matemático del derrumbamiento de bóvedas 

        en la catedral de San Pedro de Beauvais. Primer Congreso Europeo sobre Catedrales Góticas, 

        Diputación Foral de Alava, Vitoria, Spain. 

        Cundall, P. A and Hart, P. (1971). A computer model for simulating progressive large scale 

        movements in blocky rock systems. Proc. of  the Symposium of the Int. Society of Rock Mechanics, 

        Nancy, France, Vol. 1, paper No. II-8. 

        D’Ayala, D., Speranza, E. (2002)  An integrated procedure for the assessment of the seismic 

        vulnerability of historic buildings. 12th European Conference on Earthquake Engineering.  Paper n. 

        561, London. 

        De Luca , A., Giordano, A.,  Mele E. (2004)  A simplified procedure for assessing the seismic 

        capacity of masonry arches. Engineering Structures 26 (2004) 1915–1929  

        Fajfar, P. (1999) Capacity spectrum method based on inelastic demand spectra. Earthquake 

        engineering and structural dynamics, 28, 979-993. 

        Fanelli, M. (1993). Information systems for monuments and historical buildings. IABSE Symposium, 

        Structural Preservation of the Architectural Heritage, Rome, p. 65-72.  

        Ferris M, Tin-Loi F. (2001)  Limit analysis of frictional block assemblies as a mathematical program 

        with complementarity constraints. Int J Mech Sci 43, 209–24. 

        Gambarotta L., Lagomarsino S., (1997). Damage models for the seismic response of brick masonry 

        shear walls part I & part II. Earthquake Engineering and Structural Dynamics, Vol. 26. 

        Gilbert, M., Melbourne, C. (1994) Rigid-block analysis of masonry structures, The Structural 

        Engineer, 72(21),  356-361.  

        Gilbert, M. (2007) Limit analysis applied to masonry arch bridges: state-of-the-art and recent 

        developments, Arch Bridges ‘07, Funchal, Madeira, 13-28  

        Gilbert, M., Casapulla, C., Ahmed, H. M. (2006) Limit analysis of masonry block structures with non-

        associative frictional joints using linear programming. Computer & Structures, 84, 873-887. 

        Ghaboussi J., Barbosa R., (1990). Three-dimensional discrete element method for granular 

        materials, Int. J. Num. Anal. Meth. Geomech., 14, 451-472. 

        Giuffrè, A. (1990). Letture sulla Meccanica delle Murature Storiche. Kappa Ed., Rome. 

        Giuffrè, A. (1995). Vulnerability of historical cities in seismic areas and conservation criteria. 

        Congress “Terremoti e civiltà abitative”, Annali di Geofisica, Bologna   

        Giuffrè A., Carocci C., (1993), Statica e dinamica delle costruzioni murarie storiche, in Atti del 

        Convegno internazionale CNR "Le pietre da costruzione: il tufo calcareo e la pietra leccese", Mario 

        Adda Editore, Bari, pp. 539-598. 

        Gonzalez, A., Casals, A., Roca, P. and Gonzalez, J. L. (1993). Studies of Gaudi’s Cripta de la 

        Colonia Güell. IABSE Symposium, Structural Preservation of the Architectural Heritage, Rome,  

        457-464. 

        Hanganu, D. A. (1997). Análisis no Lineal Estático y Dinámico de Estructuras de Hormigón Armado 

        mediante Modelos de Daño. PhD Thesis, UPC, Barcelona.

## [p. 38]

38 

          

        Heyman, J. (1966). The stone skeleton. International Journal of Solids and Structures 2, 270-79.  

        Heyman, J. (1976). Couplet’s engineering memoirs 1726-33. History of Technology, 1, 21-44.  

        Heyman, J. (1989). Hooke’s cubico-parabolical conoid. Notes and Records of the Royal Society, 

        52 (1), 39-50.  

        Huerta, S. (2001) Mechanics of masonry vaults: The equilibrium approach. Historical Constructions, 

        University of Minho, Guimaraes, 47-69 

        ICOMOS/ISCARSAH Committee, (2005). Recommendations for the analysis, conservation and 

        structural restoration of architectural heritage. www.icomos.org 

        Karantoni,  F. V.  and Fardis,  M. N.  (1992). Effectiveness of seismic strengthening  techniques for 

        masonry buildings. J. Struct. Engrg. ASCE, 118 (7), 1884-1902. 

        Kwan, A.K.H. (1991). Analysis of Coupled Wall/Frame  Structures by Frame Method with Shear 

        Deformation Allowed. Proc. Instn Civ, Engrs., 91, 273-297. 

        Lagomarsino, S., Giovinazzi, S., Podestà, S., Resemini, S.  (2003). RISK-UE-EVK4-CT-2000-

        00014 An advanced approach to earthquake risk scenarios with application to different European 

        Towns. WP5: Vulnerability assessment of historical and monumenttal buildings. 

        Lagomarsino, S. (2006) On the vulnerability assessment of monumental buildings. Bull. Earthquake 

        Eng. 4:445-463. European Comission, Brussels. 

        Lemos, J.V. (1995). Assesment of the ultimate load of a masonry arch using discrete elements. 

        Computer Methods in Structural Masonry, 294-302. 

        Lemos J.V. (1998). Discrete element modeling of the seismic behavior of stone masonry arches, 

        G. Pande et al. (eds): Computer Methods in Structural Masonry, 4, E& FN Spon, London, 220-227. 

        Livesley, R. K. (1978). Limit analysis of structures formed from rigid blocks, Int. J. Num. Meth. 

        Engng., 12, 1853-71. 

        Lopez, J., Oller, S., Oñate, E., Lubliner, J. (1999). A homogeneous constitutive model for masonry. 

        International Journal for Numerical Methods in Engineering, 46, 1651-1671. 

        Lotfi H.R., Shing P.B. (1994). Interface model applied to fracture of masonry structures. Journal of 

        Structural Engineering ASCE, 120(1), 63-80. 

        Lourenço, P.B. (1996) Computational  strategies for masonry structures.  PhD Thesis. Delft 

        University of Technology, Delft, The Netherlands. 

        Lourenço, P. B. (1997) “An anisotropic plasticity model for quasi-brittle composite shells”. 

        Computational Plasticity: Fundamentals and Applications. Pinteridge Press, London.  

        Lourenço, P. B. and Rots, J. G. (1997). A multi-surface interface model for the analysis of masonry 

        structures. J. Engrg. Mech., ASCE, 123 (7), 660-668. 

        Lourenço, P. B., Rots, J. G., and Blaauwendraad, J. (1998). Continuum model for masonry: 

        Parameter Estimation and Validation. J. Struct. Engrg., ASCE, 1(6), 642-652. 

        Lourenço, P.B., Mourão, S. (2001). Safety assessment of Monastery of Jerónimos. Historical 

        Constructions 2001, Guimarães, 697-706.

## [p. 39]

39 

          

        Lourenço, P. B., Milani, G., Tralli, A., Zucchini, A. (2007). Analysis of masonry structures: review of 

        and recent trends of homogenisation techniques. Canadian Journal of Civil Engineering 34, 1443-

        1457. 

        Lourenço, P. B., Pina-Henriques, J. (2008) Collapse prediction and creep effects. Learning from 

        failure. Long term behaviour of heavy masonry structures. Binda, L. (Ed). WIT Press, Southampton 

        Lucchesi M., Padovani C., Pasquinelli G., Zani N. (2007). Statics of masonry  vaults, constitutive 

        model and numerical analysis. Journal of Mechanics of Materials and Structures, 2(2), 221-244. 

        Ma, M.Y.  Pan, A.D.  Luan, M. and Gebara, J.M. (1996). Seismic analysis of stone arch bridges 

        using discontinuous deformation analysis. In Proceedings of the 11th World Conference on 

        Earthquake Engineering, paper no. 1551, Amsterdam, Elsevier. 

        Macchi, G., Ruggeri, M., Eusebio, M., Moncecchi, M. (1993). Structural assessment of the leaning  

        tower of Pisa. Structural Preservation of the Architectural Heritage, IABSE, Zürich, Switzerland, 

        401-408. 

        Mallardo V., Malvezzi R., Milani E., Milani G. (2008). Seismic vulnerability of historical masonry 

        buildings: A case study in Ferrara. Engineering Structures; 30: 2223–2241. 

        Mamaghani I.H.P., Aydan O., Kajikawa Y. (1999). Analysis of masonry structures under static and 

        dynamic loading by discrete _nite element method, Structural Eng./Earthquake Eng., JSCE, 16(2), 

        75-86. 

        Mark, R., Çakmak, A. S., Erdik, M.  (1993a). Modelling and monitoring the structure of Hagia Sophia 

        in Istambul Structural. Preservation of the Architectural Heritage, Zürich, Switzerland, 179-186. 

        Mark, R., Çakmak, A. S., Hill, K, Davison, R. (1993b). Structural analysis of Haiga Sophia: a 

        historical perspective. Structural Repair and Maintenace of Historical Builsings III, Computational 

        Mechanics Publications, UK. 

        Martínez G., Roca P., Caselles O., Clapés J. (2006). Characterization of the Dynamic Response 

        for the Structure of Mallorca Cathedral. In: Lourenço P.B., Roca P., Modena C., Agrawal S., Editors, 

        Structural Analysis of Historical Constructions, New Delhi, India. 

        Massart, T.J., Peerlings, R.H.J., Geers, M.G.D. (2004). Mesoscopic modeling of failure and 

        damageinduced anisotropy in brick masonry. European Journal of Mechanics A/Solids 23, p. 719-

        735. 

        Melbourne, C. and Gilbert, M. (1994). The application of limit analysis techniques to masonry arch 

        bridges. Bridges Assessment, management and design, Editor: B.I.G. Barr, H.R.  Evans, J.E. 

        Harding, Elsevier, 193-198. 

        Meli, R., Sánchez-Ramírez, A. R. (1995). Structural aspects of the rehabilitation of the Mexico City 

        Cathedral”.  Structural analysis of historical constructions I, CIMNE, Barcelona, Spain, 123-140. 

        Meli, R., Peña, F. (2004). On elastic models for evaluation of the seismic vulnerability of masonry 

        churches. Structural Analysis of Historical Constructions, Balkema, Leiden 1121-1131. 

        Milani, G., Lourenço, P.B., Tralli (2006a). A. Homogenised limit analysis of masonry walls. Part I: 

        Failure surfaces. Computers & Structures 84(3-4), 166-180. 

        Milani, G., Lourenço, P.B., Tralli, A. (2006b). Homogenised limit analysis of masonry walls. Part II: 

        Structural applications. Computers & Structures 84(3-4), 181-195.

## [p. 40]

40 

          

        Milani, G., Lourenço, P.B., Tralli, A. (2006c). A homogenization approach for the limit analysis of 

        out-of-plane loaded masonry walls. J. Struct. Engrg., ASCE, 132, 1650-1663. 

        Milani, G., Lourenço, P.B., Tralli, A., (2007). 3D Homogenized limit analysis of masonry buildings 

        under horizontal loads. Engineering Structures, 29(11), 3134-3148. 

        Mola, F., Vitaliani, R. (1995). Analysis, diagnosis and preservation of ancient monuments: The St. 

        Mark’s Basilica in Venice. Structural analysis of historical constructions I, CIMNE, Barcelona, Spain, 

        166-188. 

        Molins C, Roca P. (1998) Capacity of Masonry Arches and Spatial Frames. Journal Structural 

        Engineering ASCE, 124(6):653-663. 

        Munjiza, A., Owen, D.R.J. and Bicanic, N. (1995). A combined finite-discrete element method in 

        transient dynamics of fracturing solids. Engineering Computations 12, 145-174. 

        Murcia-Delso, J., Das, A. K., Roca, M., Cervera, M. (2009)  Seismic safety analysis of historical 

        masonry structures using a damage constitutive model. Thematic Conference on Computational 

        Methods in Structural Dynamics and Earthquake Engineering. ???????? 

        Ngo, D., Scordelis, A. C. (1964). Finite element analysis of reinforced concrete beam. Journal of 

        American Concrete Institute, Vol. 64, 152.  

        O’Dwyer, D. (1999) Funicular analysis of masonry vaults. Computers & Structures, 73, 187-197. 

        Oñate, E., Hanganu, A., Barbat, A., Oller, S., Vitaliani, R., Saetta, A., Scotta, R. (1995). Structural 

        analysis and durability assessment of historical constructions using a finite element damage model. 

        Structural Analysis of Historical Constructions. CIMNE, 189-224. 

        Ordinanza OCPM 3274, 2003, modified according to OPM 3431, 2005.  Allegato 2, Norme tecniche 

        per il progetto, la valutazione e l’adeguamento sismico degli  edifici. Consiglio dei Ministri, Rome. 

        Orduña, A., Lourenço, P. (2003). Cap model for limit analysis and strengthening of masonry 

        structures. J. Struct. Eng. 129 (10), 1367–1375.  

        Orduña A, Lourenço, P.B. (2005a) Three-dimensional limit analysis of rigid block assemblages. Part 

        I: Torsion failure on frictional interfaces  and limit analysis formulation. International Journal of Solids 

        and Structures 42 (18-19) 5140–5160 

        Orduña, A., Lourenço, P.B. (2005b). Three-dimensional limit analysis of rigid blocks assemblages. 

        Part II: Load-path following solution procedure and validation, Int. J. Solids and Structures, 42 (18-

        19), 5161-5180  

        Ochsendorf, J.A., (2002). Collapse of Masonry Structures.  PhD thesis. Department of Engineering, 

        Univ. of Cambridge, Cambridge, UK. 

        Pagnoni T. (1994). Seismic analysis of masonry and block structures with the discrete element 

        method, Proc. 10th European Conference on Earthquake Engineering, Vol. 3, 1674-1694. 

        Pagnoni, T. And Vanzi, I. (1995). Experimental and numerical study of the seismic response of 

        block structures. Computer Methods in Structural Masonry, 213-222. 

        Papa E.A. (1996). Unilateral damage model for masonry based on a homogenization procedure. 

        Mechanics of Cohesive-Frictional Materials, 1, 349-366.

## [p. 41]

41 

                   

                Papa E., Taliercio A. (2000). Prediction of the evolution of damage in ancient masonry towers. Proc. 

                Int. Symposium ‘Bridging Large Spans from Antiquity to the Present’, Istanbul, 135-144. 

                Papastamatiou, D. And Psycharis, I. (1993). Seismic response of classical manuments –  a 

                numerical perspective developed at the Temple of Apollo Bassae, Greece. Terra Nova, 5, 591-601. 

                Pegon, P., Pinto, A.V. and Anthoine, A. (1995). Numerical simulation of historical buildings  

                subjected to earthquake loading. Structural Studies of Historical Buildings IV, 2, Computational 

                Mechanics Publications, Southampton, UK, 29-36. 

                Pegon, P., Pinto, A. V., Géradin, M. (2001) Numerical modelling of Stone-block monumental 

                structures. Computers & Structures 79, 2165-2181.  

                Pelà, L., Cervera, M., Roca, P., Benedetti, A. (2008). An orthrotropic damate model for the analysis 

                                      th

                of masonry structures. 8  Interantional Seminar on Structural Masonry ISSM 08, 175-178. 

                Pelà, L. (2009) Continuum damage model for nonlinear analysis of masonry structures. Ph.D. 

                dissertation. University of Ferrara, Ferrara. 

                Pelà, L., Aprile, A., Benedetti, A. (2009). Seismic assessment of masonry arch bridges. Engineering 

                Structures 31, 1777-1788. 

                Peña, F., Prieto, F., Lourenço, P.B., Campos Costa, A., Lemos, J.V. (2007). On the Dynamics of 

                Rocking Motion of Single Rigid–Block Structures, Earthquake Engineering and Structural 

                Dynamics. 

                Poleni, G. (1743). Memorie istoriche della gran cupola del tempio Vaticano, Stamperia del 

                seminario, Padova. 

                Psycharis, I., Lemos, J.V., Papastamatiou, D., Zambas, C. and Papantonopoulos, C. (2003). 

                Numerical study of the seismic behaviour of a part  of the Partenón Pronaos. Earthquake 

                Engineering & Structural Dynamics, 32, 2063-2084. 

                Ràfols, J.  F. (1929) Gaudí. Canosa Ed., Barcelona 

                Roca, P., Pellegrini, L., Oñate, E., Hanganu, A. (1998). Analysis of Gothic constructions. Structural 

                Analysis of Historical Constructions II. CIMNE, Barcelona. 

                Roca, P. (1998). Studies of Gaudi’s Cripta de la Colonia Güell. Structural Analysis of Historical 

                Constructions II. CIMNE, Barcelona, 377-393. 

                Roca, P.  (2001). Studies on the structure of Gothic Cathedrals. Historical Constructions, P. B. 

                Lourenço and P. Roca (Eds.), University of Guimaraes, Guimaraes.   

                Roca, P. (2004). Considerations on the significance of history for the structural analysis of ancient 

                constructions. Structural Analysis of Historical Constructions IV, Balkema, Amsterdam, 63-73. 

                Roca, P., Massanas, M., Cervera, M., Arun, G. (2004). Structural analysis of Küçük Ayasofya 

                Mosque in Ístanbul. Structural Analysis of Historical Constructions IV, Balkema, Amsterdam, 679-

                686. 

                Roca P, Molins C, Marí A. R. (2005) Strength capacity of masonry wall structures by the equivalent 

                frame method. Journal of Structural Engineering ASCE, 131(10): 1601-1610.

## [p. 42]

_(página sin capa de texto)_
