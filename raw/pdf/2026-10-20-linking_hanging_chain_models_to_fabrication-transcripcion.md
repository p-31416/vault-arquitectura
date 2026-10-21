---
tipo: transcripcion
fecha: 2026-10-20
fuente_binaria: activos/fuentes/linking_hanging_chain_models_to_fabrication/Linking Hanging Chain Models to Fabrication.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Linking Hanging Chain Models to Fabrication.pdf
titulo: Linking Hanging Chain Models to Fabrication
autor: akilian
idioma: en
paginas: 17
palabras: 5775
metodo_extraccion: ghostscript-txtwrite
aviso: "Texto con copyright - uso interno del estudio. Citar con atribucion; no redistribuir."
tags: [pdf, raw, transcripcion, gaudi, bibliografia-ai, fair-use]
---

# Transcripción — Linking Hanging Chain Models to Fabrication

> Texto extraído para análisis interno del estudio. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Linking Hanging Chain Models to Fabrication.pdf`. Binario local: [activos/fuentes/linking_hanging_chain_models_to_fabrication/Linking Hanging Chain Models to Fabrication.pdf].
> Extracción: ghostscript-txtwrite · 17 págs · 5775 palabras. Copyright del original: se cita con atribución, no se redistribuye.

## [p. 1]

Linking Hanging Chain Models to Fabrication 

                    Axel Kilian, Ph.D. Candidate in Computation, Department of Architecture, School of 

                     Architecture and Planning, Massachusetts Institute of Technology, Cambridge, MA 

                  Abstract 

                  The paper traces the development of a digital hanging chain modeler in Java inspired by 

                  Antonio Gaudi’s physical hanging chain models. More importantly, it demonstrates how 

                  fabrication schemas for physical mockups of the digitally simulated hanging chain can be 

                  linked to the real time form finding simulation. Fabrication output is an integral part of 

                  the iterative process and not a post design process. The current implementation is still 

                  limited and currently requires programming for reconfiguration. The paper proposes the 

                  link of form finding and fabrication finding and lays out several examples and first steps 

                  of how to do so. (Figure 1) 

                  Figure 1. Overview of the tool, showing mesh and string models as well as flattened 

                  patterns linked to the live form finding model 

                  1 Introduction 

                  Using physical form finding techniques as an engineering technique has precedents 

                                                                  th

                  reaching back to the Renaissance. In the early 20  century, Gaudi pioneered them as a 

                  design tool in three dimensions using hanging chain models. He produced stunning work 

                  of architecture that convince through structural and sculptural elegance. However, little is 

                  written about the process whereby the abstract string based chain model with point loads 

                  is translated into a volumetric geometry with distributed loads and structures with self-

                  weight. A weak point of Gaudi’s technique of the physical hanging chain model is to not 

                  give information on the optimal distribution of stress in the material of the built form. 

                  (Tomlow et al 1989) The author proposes some techniques to integrate this translation 

                  into the design stage of the hanging models. 

                  The paper presents a digital hanging chain model based on a particle spring systems using 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                     1

## [p. 2]

Euler and Runga Kutta solvers programmed in Java. The goal is to provide a real-time 

                    3D-modeling environment that allows the design of gravity based forms following the 

                    hanging chain principle. By using the same building components it is also possible to 

                    model any mesh topology, for instance approximations of Heinz Isler's grid shells or 

                    fabric like surfaces. The initial tool was further developed and tested in a workshop 

                    setting in order to validate results and provide a more solid implementation and input 

                    from students to the tool. The relationship between form finding model and the 

                    translation into volumetric form was explored in a series of small models. 

                    2     Motivation 

                    Physical hanging models are very compelling design devices. But a number of factors 

                    limit their use for designers. First, they need to be relatively big in scale to give accurate 

                    results and to allow measurements with reasonable tolerances. Equilibrium solutions can 

                    be scaled if the proportional distribution of mass is kept and the geometry of the lines of 

                    forces is scaled proportionally. This holds true even though mass does not scale 

                    proportionally to geometric dimensions. So the results of the physical model are usable 

                    for a full-scale building design at least as a starting point. But the amount of work needed 

                    to construct a fully detailed hanging model is enormous. Also, it is a very time 

                    consuming task to adjust the model when larger changes within its geometry occur, as the 

                    model is inherently interdependent. A small change can ripple through large parts of the 

                    model requiring adjustments which themselves cause shift elsewhere.  The model will 

                    eventually always find a state of equilibrium, but it is not guaranteed that the new state 

                    matches the desired form. This may require several iterative adjustments. 

                    The second major disadvantage is that a physical model is hard to measure accurately and 

                    in reasonable time, as measuring requires physically accessing the model. The 

                    measurement of forces within the strings of the model is even more difficult, as it 

                    requires the installation of strain gauges, which is time consuming and can potentially 

                    disturb the model. In addition, the measurements are not part of the design process. The 

                    design is frozen to allow for iterating through the load measurements throughout the 

                    model in one given state. Colonia Guell was, if one ignores a small earlier hanging 

                    model, Gaudi’s only design developed with the aid of a hanging model. The model was 

                    produced between 1898 and 1908 by a highly qualified team. (Tomlow, et al 1989) 

                    The digital version, in contrast, allows simultaneous measurement and creating/editing of 

                    geometry.  These measurements can directly drive other dimensions in the model. In the 

                    digital model, editing and creating the string weight is less limited by the availability and 

                    preparation of the physical material, which in the case of a very complex model can 

                    substantially slow down the process. Furthermore, the use of generative techniques 

                    allows for the rapid placement of complex string constructs and observing their behavior 

                    before investing time into an elaborate physical model. 

                    Finally, it is possible to create the topology of the model in a frozen state to establish the 

                    pure connectivity of the model and to then subject the model to simulated gravity and 

                    “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                               2

## [p. 3]

observe the form that emerges. This is a substantial advantage over the physical model, 

                  where gravity cannot be suppressed, which makes topological layouts harder to manage. 

                  3     Precedent for geometric constraint based construction systems  

                  3.1  Heinz Isler - Physical models for form finding measurements 

                  Since the 1950s, Swiss engineer Heinz Isler has pioneered shell structures with minimal 

                  thickness. The lines of thrust lie exactly within the thin shell cross-section. Isler extracts 

                  the geometry in a very tedious translation process from the physical scale model and 

                  scales it to full size.  Isler himself on a number of occasions came across what he thought 

                  were mistakes in the models. Isler has commented that it was a sort of not-correctness in 

                  his ideas at first, a mistake. He was unhappy that this experiment did not succeed but 

                  finally he realized that it was giving him the solution for three problems that he had not 

                  thought of. (Chilton 2000) Once the measuring is completed, it is a very time consuming 

                  process to make any alterations to the design. But physical models built in the real world 

                  also ensure that the model is not the artifact of a selective simulation strategy that may or 

                  may not include key parameters necessary to model the structure accurately. Despite the 

                  challenges they pose in achieving accuracy and scaling of material and mass, physical 

                  models do ensure a more holistic simulation of the problem than an image based 

                  computer simulation.  

                  3.2  Antonio Gaudi - The hanging model as a method of design   

                  Hanging models enable the designer to determine the optimal form of structures carrying 

                  loads purely in compression, particularly those consisting mainly of vaults. (Tomlow et al 

                  1989) Although Gaudi’s hanging models are the best known examples, previous, less 

                  sophisticated attempts at using hanging models were made by Heinrich Huebsch (1795-

                  1863) and Giovanni Poleni. (Tomlow et al 1989)  

                  The translation of the force diagram into form for some of Gaudi’s projects like Sagrada 

                  Familia (not derived with a hanging model but a plaster model) was guided by two 

                  constraints: The extrusion process of the plaster model building, and the technique of a 

                  stonemason to build surfaces with straight lines of ruling. Therefore, Gaudi’s Sagrada 

                  Familia combines two design constraint models coming from different ends. One is the 

                  overall structural geometry designed to be in equilibrium and in compression only, the 

                  other is the mode of construction using ruled surfaces only. There was a strong parallel 

                  between the work of the plaster mould-makers and the actual full-size construction of the 

                  window. In both cases, the straight lines in the ruled surfaces were used in a similar way 

                  to generate moulds. (Burry 2001) However, the hanging models do not implement the 

                  ruled surface constraints for the envelopes, and neither does the ruled surfaces rule take 

                  the distribution of masses along the structure into account. It requires an expert’s 

                  interpretation to make them work together. Gaudi saw forms and once he had determined 

                  them mentally, he sought the means to transform them into physical, buildable objects. 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                       3

## [p. 4]

(Giralt-Miracle 2002) A combination of multiple constraint models in a digital simulation 

                  would yield a wider range of exploration in both overall proportion and composition in 

                  correspondence with the surface of the building components.  

                  3.3  Frank O. Gehry - Developable surface strips for approximating freeform 

                       surfaces 

                  Developable strips for approximating freeform surfaces is another geometric constraint 

                  strategy allowing the exploration of free form while providing a building strategy. 

                  Developable surfaces are thus an important element of the arsenal of techniques used by 

                  Frank O. Gehry Associates since the early 1990s for constructability modeling. (Shelden 

                  2002) This technique is not an example of a form finding process, but rather of using 

                  geometric properties constraints. These could be linked to a form finding principle to 

                  produce structurally efficient shapes that could be built economically with sheet based 

                  materials. In Gehry’s practice, however, the form driver is not structural optimization, but 

                  sculptural expressiveness. 

                  3.4  Joerg Schlaich, Hans Schober - Quadrangular planar panel solutions for 

                       freeform surfaces 

                  The use of translation surfaces allows the fabrication of double curved surfaces with 

                  quadrangular, planar elements and constitutes a further geometric constraint modeling 

                  principle. It  has been perfected by the office of Schlaich and Bergemann since the early 

                  1990s. A robust fabrication constraint strategy is a necessity to allow for the geometric 

                  adjustments to achieve buckling resistance in the very thin glass shell domes the firm 

                  builds. This procedure allows for the use of planar glazing and plane formwork elements, 

                  a major prerequisite for the economic realization of glazed, opaque or concrete spatial 

                  structures. (Schober 2002) 

                  4 Catenary simulation 

                  4.1  Equation based catenaries 

                  It is possible to calculate a catenary curve between two support points given a string 

                  length based on a parametric equation. (Figure 2) The hyperbolic cosine,  

                                       

                  Figure 2. Catenary equation and family of catenary curve plots (Weisstein 1999) 

                  forms the basis for the catenary equation and allows the calculation of any point on a 

                  hanging string of uniform weight, which is supported at two points. Where t = 0 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                     4

## [p. 5]

corresponds to the vertex, and a is a parameter that determines how quickly the catenary 

                  "opens up." (Weisstein 1999) The amount of "sagging" is related to the string length and 

                  the distance between the supports. The equation can be adapted to uneven support points 

                  as well. Paul Cella noticed that textbooks of mathematics, mechanics and engineering 

                  practice produced what appeared to be a settled conclusion: When the supports of a 

                  catenary are at different elevations the mathematical complexity precludes a theoretically 

                  correct solution and a parabolic approximation is the recommended approach. (Cella 

                  1999) He subsequently derived the catenary equations to calculate the uneven support 

                  catenary problem. (Figure 3) 

                  Figure 3. Calculation of a catenary curve between uneven supports (Cella 1999) 

                  What the catenary equation based approach does not provide is a way of solving 

                  undetermined structures, for instance if four strings are joined in one node and no single 

                  solution exists. The subparts of the catenary between support points can still be solved 

                  equation-based, but the location of the supports in the general case can only found 

                  through a solver-based approach. This is where the use of a solver is necessary in order to 

                  determine the overall geometry for the equilibrium of forces in the structure. 

                  4.2  The computational model used for simulating hanging models 

                  A more general approach to the problem is using a particle-based approach that 

                  represents a punctual mass in space and has a position and velocity as well as an 

                  acceleration property. Based on Newton’s law, a force acting on a body causes 

                  acceleration, which is inversely proportional to the mass of the body in the direction the 

                  force is applied. We can formulate a system of equations that can be integrated 

                  analytically to solve for the position of a point mass with respect to time. With the 

                  introduction of gravity, linear spring force and viscous drag it is possible to construct a 

                  particle spring system with simulated gravity. For the simple determined cases, analytical 

                  integration works. But in more complex cases, it is necessary to integrate numerically. 

                  Different methods have been developed, among them Euler method, midpoint, Runga 

                  Kutta. (Baraff and Witkin 1999)  

                  The author used an explicit Euler solver for mesh simulation, which is satisfactory for 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                     5

## [p. 6]

relatively low stiffness of the springs. During a workshop at MIT in the Spring of 2004 

                  conducted by John Ochsendorf, Axel Kilian, Barbara Cutler, Eric and Marty Demaine, a 

                  second implementation was written which can handle meshes with very high stiffness and 

                  uses an implicit version of Euler and Runga Kutta to get stable solutions. Cloth strongly 

                  resists stretching motions while being comparatively permissive in allowing bending or 

                  shearing motions. This results in a “stiff” underlying differential equation of motion. 

                  (Press et al 1986) Explicit methods are ill-suited to solving stiff equations because they 

                  require many small steps to stably advance the simulation forward in time. (Baraff and 

                  Witkin 1998) Strings in the hanging model have similar characteristics as cloth as they 

                  have very stiff, meaning non-stretching segments making up the string. 

                  This computational method allows the interactive construction of string like constructs 

                  out of particles and spring elements that approximate physical hanging model behavior 

                  when subjected to gravity. This approach is not new but well established in the computer 

                  graphics community and the animation industry. Novel is to use it as an interactive 

                  modeling environment for designers that allows not only optimization but also playful 

                  exploration of the evolving structure. The system is being referred to either as mass 

                  spring system or particle system. For the remainder of the paper the term Particle Spring 

                  system will be used. 

                  5     Translation from an abstract string model to a volumetric envelope 

                  Architects who have used hanging models struggled with the translation of the two-

                  dimensional elements of the network of strings into the complex spatial curvature of the 

                  three-dimensional surfaces necessary to stay true to the model. In “Das Model” it is 

                  stated, “Apparently as a side effect of this struggle to follow constructional forms based 

                  on hanging models, for the first time in architectural history the hyperbolic paraboloid 

                  form was tried out in a building.” (Tomlow et al 1989) 

                  The hanging model provides a line model for the load paths for a given distribution of 

                  weight. However, it does not specify where the envelope lies in correspondence to the 

                  load path.  

                  In general, the self-weight of the load-bearing member contributes only negligible 

                  amounts to the structure locally and therefore does not substantially affect the hanging 

                  curve form. If there is no load present other than the weight of the structure itself, the 

                  self-weight becomes the dominant form giving factor. The cross section has to provide 

                  enough area for the forces traveling through it. A further optimization of the structure, for 

                  example with the aim of achieving uniform compressional loading throughout the same 

                  material, which would be possible by varying thickness, was not undertaken by Gaudi. 

                  (Tomlow et al 1989) 

                  The digital hanging model presented here does create varying thickness of the extrusion 

                  along the members based on the forces present in each member. The resolution of the 

                  simulation is also a factor in determining the volumetric form. In order to keep the 

                  number of particles in the simulation low, the number of particles a hanging line is 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                       6

## [p. 7]

usually relatively low. (Figure 4) This leads to polyline forms with straight spring 

                  sections in between. If the resolution is too low, it significantly offsets the load path from 

                  the ideal catenary. In a later version, dynamic subdivision of the springs based on offset 

                  measurements from the ideal catenary will be implemented. 

                  Figure 4. Hanging chains with varying subdivisions of particles (left). The hanging 

                  chain approximates the catenary. Some stretch occurs due to non-stiff springs due 

                  to the explicit solver (right). 

                  5.1 Linear extrusion 

                  The most straightforward translation from the line skeleton into a volumetric entity is an 

                  extrusion of a profile along the spring vectors with its diameter being approximately 

                  scaled to the forces present in the particular section of the string. Additional factors for 

                  determining the cross section are local and global buckling. (Figure 5) 

                  The shape of the extrusion can be varied to produce different cross sections depending on 

                  what material is being used. The load path must lie completely within the geometric 

                  envelope in order to keep the structure in equilibrium. Furthermore, if the material cross 

                  section is not supposed to be subject to tension, the load path has to lie within the 

                  innermost third of a symmetrical cross section.  

                  A bigger question is the development of the intersection between members of differing 

                  cross sections and spatial orientations. At acute angles, the intersections can become quite 

                  large in comparison to the members themselves and create difficulties in applying a 

                  uniform joint system. Parametric studies have been done to study joint systems to take 

                  this variation into account. (Figure 6) 

                  Figure 5. Different linear translation strategies programmatically linked to the form 

                  finding path: (a) path only, (b) square extrusion scaled to allowable stresses, (c) 

                  round section and ball points and unfolded cylinder surfaces 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                     7

## [p. 8]

Figure 6. Joint studies from a previous project for intersections of members of 

                  unequal diameter in different spatial configurations using a parametric 

                  representation 

                  5.2  Grid mesh strategies  

                  As soon as the springs form a network that is more than a linear linked chain of springs 

                  and particles the structural behavior becomes more complex. No longer is there one 

                  unique load path. Multiple paths between support and loads are possible and no single 

                  determined solution exists. Also, the behavior approximates that of a shell with 

                  increasing mesh density. An additional artifact of the simulation approach becomes 

                  apparent, as the spring approach does not ensure tension only members. If the distance 

                  between two particles falls below the rest length of the spring the spring generates 

                  compression forces. Detecting the state of the spring at any point and alerting the viewer 

                  of its compression state or alternatively removing it from the solution can avoid this 

                  problem. 

                  In determining the thickness of shells that are approximated by grid meshes one can refer 

                  to Heinz Isler’s work. Isler identifies instabilities in his shells as follows: First, at the 

                  supports second, due to general buckling; third, due to local buckling of the free edge (for 

                  which the counter curvature is so important); and finally, due to other modes. (Chilton 

                  2000) Isler gives his general equation for shell buckling as  

                  Pk = c E (t/r)^x  >= s Peff   

                  (Pk critical buckling load, c a modification factor, E modulus of elasticity, t shell 

                  thickness, r local radius of curvature, x power of curvature, s safety factor) (Chilton 

                  2000) 

                  The author explored a less rigorous, visual approach to testing the stability of a simulated 

                  form. By adding additional forces besides the vertical force of gravity, the structures can 

                  be triggered to sway. (Figure 8) The relative amount of swaying of each particle is traced 

                  for the previous 200 positions. This allows a visual comparison of the displacement of the 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                     8

## [p. 9]

structure in different areas. Stable structures will show little, uniform displacements. 

                  Instability becomes apparent when traces vary widely. This approach could be developed 

                  further to integrate proper wind load and earthquake displacements. For now it is an 

                  interactive, non complex way to explore a form for structural redundancy beyond one 

                  optimal load case. 

                  Figure 7. Simple instability test through varying gravity and tracing the position of 

                  each particle through a history trace 

                  5.3  Integration of form finding and construction constraints into design 

                  As illustrated in the precedent examples of Isler, Gehry, Schlaich and Gaudi, the 

                  integration of construction constraint approaches is generally solved in the following 

                  way: The form finding process defines the overall geometry, i.e. the skeleton of the 

                  structure, whereas the constraint geometries ride on top of the primary geometry, solving 

                  their constraints with regards to the overall geometry. Ideally, this combination results in 

                  constructible and structurally feasible geometries that allow the designer to focus on the 

                  expression of the overall design. In reality, the material properties rarely factor into the 

                  form finding process in design. 

                  Some recent work in the area of tensile structures has addressed the integration of 

                  material properties into form finding and pattern generation. One method determines 

                  cutting patterns of membrane structures by taking into account the materials’ 

                  viscoelasticity. (Fujiwara, Ohsaki, Uetani 2001) 

                  The question is how much designer input is required at the early stages of design. While 

                  the designer should not be over-constrained in her or his freedom, the designer should not 

                  be overwhelmed with too specific input requests when still in the explorative stage of the 

                  design process.  

                  6 Examples 

                  6.1  Validation examples of the hanging model 

                  In order to validate the results of the digital hanging model, physical models of the 

                  digitally derived geometry were built and subjected to proportional the same load 

                  distribution as simulated in the digital model. A comparison of the geometries proved the 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                     9

## [p. 10]

model to be satisfactorily close to the model constructed on the basis of the digital model. 

                   

                  Figure 8. Physical hanging model test. (left) Paper tubes constructed on the basis of 

                  the digital model (right) The physical hanging model based on the same dimensions. 

                  6.2  Roof example  

                  An example model was produced from a digital hanging model and fabricated to validate 

                  the approach. For the translation of the wire frame model into a surface, rhino was used 

                  as an intermediary. 

                  The physical model was subjected to vertical loads similar to the forces in the form 

                  finding simulation and the response of the supports was observed. The deflection due to 

                  the accumulated loads of the shell clearly shows at the two middle supports of the roof in 

                  the physical model, which corresponds to the force distribution in the form finding 

                  model. In addition, the physical model clearly demonstrates the structure’s vulnerability  

                  to forces other then gravity. When the structure is loaded laterally, it is much more elastic 

                  in its response than under a vertical load and does not act as a shell.  

                  Figure 9. Roof example design using a wireframe based form finding approach with 

                  subsequent lofting and flattening for fabrication of the physical panels 

                  7     Designing in dynamics vs. analytical approach. Design by discovery 

                  Current design software supports the creation of geometry through geometric operations 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                      10

## [p. 11]

aimed at creating solids, wireframe and surfaces. This geometry captures the design 

                  intention to a point and serves as the communication platform for many interdisciplinary 

                  discussions. Structural analysis is usually done using this geometry, or on specifically 

                  created geometry based on it. This analytical step requires a relatively large investment of 

                  time and does not easily allow the designer to go back and change things. In addition, the 

                  results of the analysis do not immediately provide a remedy for correcting a potential 

                  problem.  

                  This is where the learning by discovery enabled by interactive tools comes into play. In 

                  interaction with a live, force-geometry linked structure, a designer can directly observe 

                  the range of structural responses while exploring possible forms. This encourages an 

                  explorative approach to design and supports unconventional solutions that integrate and 

                  respond to the designer’s intent.  

                  Structural and dimensional evaluation of form is not an afterthought but an essential of 

                  the design process. Innovative structural solutions for shapes that are not limited to post 

                  and beam convention require innovative translation of the design intent. Structural 

                  behavior of complex form is hard to predict. Therefore, the ability for early structural 

                  feedback is important. Discovery of design in interaction with the tool rather than 

                  optimization of early design sketches. Iterative back and forth between design moves and 

                  a structural response allow for integration of the structural properties. Varying degrees of 

                  optimization – The design goal cannot possibly be driven by optimal structural shapes 

                  only – designer has a choice to go less efficient. 

                  Figure 10. Two stage design: (a) constructing the mesh in a frozen state, (b) starting 

                  the simulation 

                  8     Form finding should not be applied isolated from material distribution 

                  To approach from finding from a design point of view it is necessary to expand the scope 

                  beyond optimizing a given geometry. A combination of form finding, topology finding, 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                      11

## [p. 12]

load path finding, material distribution and testing for structural redundancy will give a 

                  much wider range of possible outcomes and allows for designer choice in the 

                  optimization. 

                  8.1 Load path 

                  The load paths in a structure are very much dependent on the topology of the mesh and 

                  the geometry of the individual members. Often a topology change to avoid a singular 

                  dominant load path does much more to make a form more efficient then the geometric 

                  optimization of the starting topology. For instance Isler was surprised to find that 90% of 

                  the loads in his shells are traveling into the supports in the corners of his shells. The edge 

                  supports get only a fraction of the weight. This has to do with the different stiffness of the 

                  shell areas and subsequent variant resistance to loading. Therefore optimizing 

                  compression-only structures does not guarantee evenly distributed loads. In order to 

                  achieve uniformly distributed loads in a structure the thickness has to be adapted in 

                  accordance to the loads present after the initial form finding.  

                                               

                  Figure 11. Load paths emerge through form finding (load proportional to the area 

                  of the cross section) 

                  8.2 Mesh topology 

                  The mesh topology has a substantial effect on the form of the structure and on the 

                  distribution of forces within it. The mesh topology fundamentally influences the 

                  performance of the structure. To optimize a structure cannot only mean to find the most 

                  efficient form for a given topology, but to find the most optimal topology for a given load 

                  case. This introduces the notion of topology finding or structure generation in addition to 

                  form finding. 

                   

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                    12

## [p. 13]

Figure 12. Variations on possible meshes for a dome with a square footprint 

                  Figure 13. Details of different mesh patterns for a square footprint 

                  8.3 Volumetric distribution 

                  Adding material in response to the forces that need to be handled may affect the load 

                  distribution if the required cross section does not correspond with the load initially placed 

                  for the member. In most cases, the member weight will be insignificant compared to the 

                  load traveling through it. But there might be cases where another iteration of adjusting 

                  the form to the new load scenario is necessary. Minimum dimensions necessary for 

                  construction might also limit the ability to exactly match the load distribution in the 

                  abstract model. 

                  8.4  Solid extrusions vs. hollow structure 

                  The load path does not have to be embedded in material as long as the center of gravity of 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                    13

## [p. 14]

the cross section corresponds approximately to the location of the load path. This was 

                  already realized in domes in the Renaissance and used for double shell construction. This 

                  principle is well established in space frame and truss design where the tension member 

                  and the compression member are separated by a void that is connected through diagonals. 

                  9     Optimization as a part of design 

                  The notion of optimization as a design support tool is questionable if it remains 

                  unchecked. Initial design moves often are exploratory in nature and may or may not have 

                  an impact on the eventual outcome. To optimize an intermediary design move may cause 

                  paths to be abandoned or curtailed prematurely. It maybe more appropriate to speak of 

                  discovery rather then optimization. Design discovery could be defined as opening up 

                  potential design paths to the designer in the light of environmental influences acting on 

                  the design such as for instance gravity. The effect of such external parameters on the 

                  design may be mediated or weighted accordingly. 

                  Optimization should not be the sole driver in design, as choosing an optimization 

                  objective is already part of the design choice. To choose a goal is to set a design process. 

                  Although it might seem like structural performance and material usage are out of the 

                  question for design considerations, some of the most radical differences in design 

                  approach constitute themselves in the differing positions on structural rational and 

                  material efficiency. What often is missing in design optimization is the variation of the 

                  starting premise.  

                  Kristina Shea’s Eifform is one of the few examples where the optimization is coupled to 

                  a generative technique, allowing the recreation of the structure topology based on the 

                  performance analysis. (Shea and Cagan 1997) Currently the form finding tool in 

                  development based on the workshop does some dynamic editing of the mesh topology 

                  based on tension/compression distribution in the structure. If a strut goes into 

                  compression it is eliminated. Over the course of the simulation only struts in tension 

                  remain. 

                  More research into the dynamic topology response is needed along the lines of Kristi 

                  Shea’s research in order to make optimization a true component of design exploration 

                  and to allow for direct intervention by the designer. 

                  10  The results of the workshop 

                  In the spring semester of 2004, instructors and students from civil engineering, 

                  architecture, computer science and computer graphics conducted a workshop to 

                  investigate the problem from an interdisciplinary perspective. 

                  A robust and scalable implicit solver was implemented in C++. It allows the handling of 

                  larger particle spring meshes and faster processing times. The application was tested in its 

                  initial stages and will be applied in a design context in the near future. For validation 

                  purposes a spherical roof shell structure was modeled and evaluated in the software. 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                      14

## [p. 15]

Figure 14. C++ implementation of an implicit solver,  the outcome of the workshop, 

                  showing a spherical dome before and after releasing it to gravity 

                  11 Conclusion 

                  The paper lays out the potential for the integration of form finding techniques with 

                  fabrication strategies in a digital, integrated, expandable environment.  

                  Form finding techniques in an interactive digital modeling environment can support the 

                  design process by giving continuous feedback to the designer, allowing the designer to 

                  integrate structural principles into the creation of form rather than to structurally optimize 

                  the finished form at the end of the design process. Digital simulation makes a range of 

                  numerical outputs of the form available for the generation of additional geometric 

                  information (like a building envelope) in response to the forces present. However, the 

                  approach to design should not a priori be driven by form finding or structural 

                  optimization. The design tools should always allow the designer to intervene and define 

                  design optimization principles.  

                  It is certainly not the goal of the approach outlined in this paper to promote a certain style 

                  or to create a “Gaudi design machine”. The goal is to understand that  expressing design 

                  goals as computational principles can support interactive design exploration and enhance 

                  the design experience. If the tools can provide a higher level of sophistication in doing so 

                  and enable handling complex competing design constraints in an interactive way, they 

                  will stimulate and challenge the notion of the design process in modeling environments 

                  today.  

                  12 Future work 

                  The tool will be further developed and tested in a design studio and structures class. A 

                  larger research goal is the reversal of the design direction. For instance can fabrication 

                  issues or patterns drive the form finding process? Gaudi’s compression only structural 

                  geometry might be competing with ruled surface construction constraints.  A way to 

                  integrate both would be ideal - a balance between the structural efficiency, the 

                  construction constraints and the distribution of mass in correspondence to the overall 

                  structure would be ideal. 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                    15

## [p. 16]

13 Acknowledgments 

                  I would like to thank the initiator of the Spring 2004 MIT workshop Prof. John 

                  Ochsendorf and my co-instructors Dr. Barbara Cutler, Prof. Eric Demaine, Marty 

                  Demaine and Simon Greenwold as well as the workshop participants who collaborated to 

                  create the C++ application. The students were Ryo Shimizo, Eric Tung, Emily Vincent, 

                  Philippe Block, Amanda Parkes, Kyle Steinfeld , Sotirios Kotsopoulos. Participants and 

                  instructors of the interdisciplinary workshop were from architecture, computer science, 

                  civil engineering and computer graphics. An earlier 2D version of the tool was developed 

                  by the author together with Dan Chak and Megan Galbraith in the fall of 2002. The java 

                  programming for the prototype shown here was done in processing, a 3D programming 

                  environment developed for the design community by Benjamin Fry and Casey Reas at 

                  the MIT Media Lab, Cambridge, USA. The workshop will be continued in the fall of 

                  2004. 

                  References 

                  Baraff, D., Witkin A., (1998), Large Steps in Cloth Simulation. Computer Graphics 

                       Proceedings, Annual Conference Series, pp 43-54 

                  Baraff, D., Witkin A., (1999), Physically-based modeling, SIGGRAPH Course Notes 

                  Burry, M., (2001), Machine-Readable Models to Interpret and Explain Gaudí's Use of 

                       Ruled-surface Geometries, in: The proceedings of CAADRIA 2002: Redefining 

                       Content 

                  Cella, P., (1999), Reexamining the Catenary, in: The College Mathematics Journal, 

                       Volume 30, Number 5, pp 391-393 

                  Fujiwara, J., Ohsaki, K., Uetani, K., (2001), Cutting pattern design of membrane 

                       structures considering viscoelasticity of material, Proceedings of IASS Symposium 

                       on Theory, design and realization of shell and spatial structures, Nagoya, Japan 

                  Giralt-Miracle, D., (2002), Gaudí. Exploring form space, geometry, structure and 

                       construction, Planeta Pub Corp, Barcelona, Spain 

                  Press, W.H., Flannery, B.P., Teukolsky, S.A., and Vetterling, W.T., (1986), Numerical 

                       Recipes, Cambridge University Press 1986. 

                  Schober, Dr. Ing. H., (2002), Geometry principles for economical and efficient shell 

                       structures, Bautechnik 79, H. 1, S. 16-24, Verlag Ernst & Sohn, Berlin, Germany 

                  Shea, K., Cagan, J., (1996), Innovative Dome Design: Applying Geodesic Patterns with 

                       Shape Annealing, accepted for publication in: Artificial Intelligence for 

                       Engineering Design, Analysis, and Manufacturing 

                  Shelden, D., PhD, (2002) Digital Surface Representation and the Constructability of 

                       Gehry’s Architecture, PhD MIT, September 2002, Cambridge, MA 

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                    16

## [p. 17]

Tomlow, J., Graefe, R., Otto, F., Szeemann, H., (1989), Das Modell,  The Model, Institut 

                       für Leichte Flächentragwerke, Stuttgart, Germany  [Edition in German, English and 

                       Spanish.] 

                  Weisstein, E., Catenary From MathWorld, A Wolfram Web Resource. 

                       http://mathworld.wolfram.com/Catenary.html 

                   

                   

                  “Linking Hanging Chain Models to Fabrication” Axel Kilian, MIT                    17
