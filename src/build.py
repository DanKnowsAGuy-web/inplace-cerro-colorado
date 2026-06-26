# -*- coding: utf-8 -*-
# Builds index.html from the bilingual content tables below.
# Images are referenced from assets/img/ (regenerate them with extract_images.py).
# Run from anywhere:  python3 src/build.py
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def im(key, cls='', alt=''):
    return f'<img class="lz {cls}" src="assets/img/{key}.jpg" loading="lazy" alt="{alt}">'

def L(lang):
    en = lang=='en'
    return {
    # cover / hero
    'tagline':'Your Groundwork Strategist',
    # full report strings
    'fr_eyebrow': 'Complete Field Study / Full Translation' if en else 'Estudio de Campo Completo / Informe Íntegro',
    'fr_sub': ("The full 2018 municipal engineering report for the Añashuayco road, translated and rebuilt in full. Independent CBR testing, complete quantities and costs, construction record, field photography, and the signed laboratory certificates. Nothing removed."
        if en else
        "El informe municipal de ingeniería de 2018 para la vía Añashuayco, traducido y reconstruido en su totalidad. Ensayos CBR independientes, metrados y costos completos, registro de obra, panel fotográfico y los certificados de laboratorio firmados. Nada omitido."),
    'm_loc':'Location' if en else 'Ubicación', 'm_loc_v':'Arequipa, Peru' if en else 'Arequipa, Perú',
    'm_year':'Year' if en else 'Año',
    'm_area':'Surfaced Area' if en else 'Área Pavimentada',
    'm_owner':'Owner' if en else 'Entidad', 'm_owner_v':'Municipality of Cerro Colorado' if en else 'Municipalidad de Cerro Colorado',
    # toc
    'toc':[ (en and t or s) for t,s in [
        ('The Result That Matters','El Resultado que Importa'),
        ('The Project','El Proyecto'),
        ('Independent CBR Testing','Ensayos CBR Independientes'),
        ('Cost Comparison','Comparación de Costos'),
        ('Construction Method','Método Constructivo'),
        ('Quantities, Planned vs Built','Metrados, Programado vs Ejecutado'),
        ('Valued Resource Summary','Resumen Valorizado de Recursos'),
        ('Engineering Conclusion','Conclusión de Ingeniería'),
        ('Field Photography','Panel Fotográfico'),
        ('Engineering Drawings','Planos'),
        ('Laboratory Certificates','Certificados de Laboratorio')]],
    # preface
    'pre_label':'A Note on This Document' if en else 'Nota sobre este Documento',
    'pre_p1': ("This is a complete translation and redesign of the 2018 final engineering report for a road project in Cerro Colorado, Peru, prepared under direct administration by the Municipality of Cerro Colorado. Every section of the original is carried through, including the quantities, valuations, construction record, photographs, and the signed laboratory certificates reproduced in full at the end."
        if en else
        "Esta es una traducción y rediseño completos del informe final de ingeniería de 2018 para un proyecto vial en Cerro Colorado, Perú, ejecutado por administración directa de la Municipalidad de Cerro Colorado. Se conserva cada sección del original, incluyendo los metrados, las valorizaciones, el registro de obra, las fotografías y los certificados de laboratorio firmados reproducidos íntegramente al final."),
    'pre_p2': ("One correction runs throughout. The original report describes the material as a polymer. It is not. In-Place BaseGrade is a certified, 100 percent organic binder. In the original it also appears under earlier names, SSPMB and Sta'bl-Soil, before the brand was finalized. The product is referred to here by its current name and its true classification. All measurements, test values, and figures are reproduced exactly as recorded."
        if en else
        "Una aclaración recorre todo el documento. El informe original describe el material como un polímero. No lo es. In-Place BaseGrade es un aglutinante certificado 100% orgánico. En el original también aparece bajo nombres anteriores, SSPMB y Sta'bl-Soil, antes de fijarse la marca. Aquí el producto se nombra por su denominación actual y su verdadera clasificación. Todas las mediciones, valores de ensayo y cifras se reproducen exactamente como fueron registrados."),
    # s1
    's1_eyebrow':'The Result That Matters' if en else 'El Resultado que Importa',
    's1_h':'The base outperformed the standard it had to meet.' if en else 'La base superó el estándar que debía cumplir.',
    's1_lead': ("CBR is the worldwide measure of whether ground can carry heavy traffic over time. For this corridor's traffic class, Peru's national road manual sets a demanding minimum. The untreated native base scored well below it. Treated in place, the same material rose past the requirement and kept climbing with richer binder ratios."
        if en else
        "El CBR es la medida mundial de si un terreno puede soportar tráfico pesado en el tiempo. Para la clase de tráfico de esta vía, el manual de carreteras del Perú fija un mínimo exigente. La base natural sin tratar quedó muy por debajo. Tratado in situ, el mismo material superó el requisito y siguió subiendo con proporciones de aglutinante más ricas."),
    'tb_label':'CBR at 100% Maximum Dry Density / NTP 339.145' if en else 'CBR al 100% de la Máxima Densidad Seca / NTP 339.145',
    'cbr_rows':[
        ('Native base, untreated' if en else 'Base natural, sin tratar', '75% screened fill plus 1/2" stone' if en else '75% afirmado más piedra 1/2"', 68,'b-base',52),
        ('Treated, 1:7 ratio' if en else 'Tratado, proporción 1:7', 'The field mix used on this project' if en else 'La mezcla usada en obra', 98,'b-mid',75),
        ('Treated, 1:8 ratio' if en else 'Tratado, proporción 1:8', 'Higher binder proportion' if en else 'Mayor proporción de aglutinante', 120,'b-hi',92),
        ('Treated, 1:9 ratio' if en else 'Tratado, proporción 1:9', 'Highest binder proportion tested' if en else 'Mayor proporción ensayada', 125,'b-hi',96)],
    'tb_thresh': ('EG-2013 minimum for TP6 high-volume traffic (1,702,886 ESAL): <b>100% CBR</b>. The native base reached 68 percent. Treatment lifted it past the line.'
        if en else
        'Mínimo EG-2013 para tráfico TP6 de alto volumen (1,702,886 EE): <b>100% CBR</b>. La base natural alcanzó 68%. El tratamiento la elevó por encima del límite.'),
    's1_p': ("The field crew selected the 1:7 ratio as the most economical mix that still met the structural target, dosed at 0.589 gallons per square meter. A field density test on the finished base reached <strong>102 percent</strong> of the compaction grade."
        if en else
        "El equipo de obra eligió la proporción 1:7 como la mezcla más económica que aún cumplía el objetivo estructural, dosificada a 0.589 galones por metro cuadrado. Un ensayo de densidad de campo sobre la base terminada alcanzó el <strong>102 por ciento</strong> del grado de compactación."),
    'pct':'%','m':'m','cm':'cm',
    'days':'days' if en else 'días',
    # s2
    's2_eyebrow':'The Project' if en else 'El Proyecto',
    's2_h':'One corridor, treated in place, finished in days.' if en else 'Una vía, tratada in situ, terminada en días.',
    's2_p': ("The Municipality of Cerro Colorado carried out maintenance on the carriageway running parallel to the Arequipa to Yura road, Stage II, at the entrance to the Añashuayco bridge, opposite APTASA. The work was executed under direct administration by the contractor LRB Corporación Minera S.A.C. The goal was to convert the existing soil into a load-bearing structure capable of carrying light and heavy vehicular traffic."
        if en else
        "La Municipalidad de Cerro Colorado realizó el mantenimiento de la vía carrozable paralela a la vía Arequipa - Yura, II Etapa, a la entrada del puente Añashuayco, frente a APTASA. La obra se ejecutó por administración directa con la empresa LRB Corporación Minera S.A.C. El objetivo fue convertir el suelo existente en una estructura portante capaz de soportar tránsito vehicular liviano y pesado."),
    's2_stats':[
        (310,'m','Corridor length treated and surfaced' if en else 'Longitud tratada y pavimentada'),
        (15,'cm','Base depth, with no sub-base required' if en else 'Espesor de base, sin sub-base'),
        (6,('days' if en else 'días'),'Total execution window on site' if en else 'Plazo total de ejecución en obra'),
        (102,'%','Field compaction grade achieved' if en else 'Grado de compactación alcanzado')],
    's2_record':'Project Record' if en else 'Ficha del Proyecto',
    'rec':[ (a if en else b, c if en else d) for a,b,c,d in [
        ('Owner','Entidad','Municipality of Cerro Colorado, Arequipa, Peru','Municipalidad de Cerro Colorado, Arequipa, Perú'),
        ('Contractor','Contratista','LRB Corporación Minera S.A.C.','LRB Corporación Minera S.A.C.'),
        ('Authorization','Resolución de aprobación','Management Resolution No. 004-2018-GOPI-MDCC','Resolución de Gerencia N° 004-2018-GOPI-MDCC'),
        ('Financing source','Fuente de financiamiento','Determined Resources','Recursos Determinados'),
        ('Execution','Modalidad de ejecución','Direct administration','Administración Directa'),
        ('Dates','Fechas','September 29 to October 10, 2018','29 de septiembre al 10 de octubre de 2018'),
        ('Length, executed','Longitud ejecutada','310.00 m (300.14 m programmed)','310.00 m (300.14 m programado)'),
        ('Surfaced area, executed','Área pavimentada ejecutada','1,922.00 m² (1,920.90 m² programmed)','1,922.00 m² (1,920.90 m² programado)'),
        ('Native soil classification','Clasificación del suelo natural','A-1-b, sandy silty','A-1-b, arenoso limoso'),
        ('Inspector of works','Inspector de obra','Eng. Enrique Iturry','Ing. Enrique Iturry'),
        ('Deputy manager, maintenance and roads','Subgerente de Mantenimiento y Vías','Arch. Leonel Ronald Ancco Mamani','Arq. Leonel Ronald Ancco Mamani'),
        ('Approved budget','Presupuesto aprobado','S/ 96,286.39','S/ 96,286.39'),
        ('Executed cost','Presupuesto de ejecución','S/ 70,297.76','S/ 70,297.76'),
        ('Budget balance','Saldo presupuestal','S/ 25,988.63','S/ 25,988.63'),
        ('Physical completion','Avance físico','100%','100%')]],
    # s3
    's3_eyebrow':'Independent Verification' if en else 'Verificación Independiente',
    's3_h':'The numbers came from an accredited laboratory.' if en else 'Las cifras provienen de un laboratorio acreditado.',
    's3_p': ("The road was evaluated both functionally and structurally through CBR testing across a range of binder proportions, from 1:3 through 1:9. Testing was performed by an independent soil mechanics laboratory accredited to ISO/IEC 17025, the international standard for testing competence. The signed certificates are reproduced in full in Section 11."
        if en else
        "La vía se evaluó funcional y estructuralmente mediante ensayos CBR en un rango de proporciones de aglutinante, de 1:3 a 1:9. Los ensayos los realizó un laboratorio independiente de mecánica de suelos acreditado ISO/IEC 17025, el estándar internacional de competencia de ensayo. Los certificados firmados se reproducen íntegros en la Sección 11."),
    'cred_org':'Testing Laboratory' if en else 'Laboratorio de Ensayo',
    'cred_sub': ("Soil mechanics testing, accredited to ISO/IEC 17025. Arequipa, Peru. Signed by Roberto B. Cáceres Flores, Civil Engineer, CIP 59876."
        if en else
        "Ensayos de mecánica de suelos, acreditado ISO/IEC 17025. Arequipa, Perú. Firmado por Roberto B. Cáceres Flores, Ingeniero Civil, CIP 59876."),
    'cred':[ (a if en else b, c if en else d) for a,b,c,d in [
        ('Test Standard','Norma de Ensayo','NTP 339.145 : 1999 (CBR)','NTP 339.145 : 1999 (CBR)'),
        ('Design Reference','Referencia de Diseño','Road Manual EG-2013','Manual de Carreteras EG-2013'),
        ('Traffic Class','Clase de Tráfico','TP6, high volume','TP6, alto volumen'),
        ('Design Loading','Carga de Diseño','1,702,886 ESAL (1.70E+06)','1,702,886 EE (1.70E+06)'),
        ('Sample Source','Procedencia de la Muestra','Añashuayco, 75% fill plus 1/2" stone','Añashuayco, 75% afirmado más piedra 1/2"'),
        ('Requested by','Solicitado por','Eng. José Luis Calcina Calcina','Ing. José Luis Calcina Calcina'),
        ('Received / Tested','Recepción / Ejecución','Oct 5 / Oct 16, 2017','05/10 / 16/10 de 2017'),
        ('Report Series','Serie de Informes','AM 389.1 through 389.4','AM 389.1 a 389.4')]],
    's3_t1':'CBR by Compaction Energy, All Mixes' if en else 'CBR por Energía de Compactación, Todas las Mezclas',
    'th_mix':'Mix' if en else 'Mezcla',
    'th_blows':'blows' if en else 'golpes',
    'th_cbr100':'CBR @ 100% MDD' if en else 'CBR al 100% MDS',
    'th_cbr95':'CBR @ 95% MDD' if en else 'CBR al 95% MDS',
    'cbr_table':[
        ('Native, untreated' if en else 'Natural, sin tratar',32.0,51.0,68.0,'68%','32%'),
        ('Treated 1:7' if en else 'Tratado 1:7',42.0,75.0,98.0,'98%','50%'),
        ('Treated 1:8' if en else 'Tratado 1:8',32.0,69.0,120.0,'120%','47%'),
        ('Treated 1:9' if en else 'Tratado 1:9',43.0,99.0,125.0,'125%','58%')],
    's3_t2':'Density and Moisture at Test' if en else 'Densidad y Humedad en el Ensayo',
    'th_mdd':'Max dry density (g/cm³)' if en else 'Máx. densidad seca (g/cm³)',
    'th_moist':'Moisture at 56 blows' if en else 'Humedad a 56 golpes',
    'th_exp':'Expansion' if en else 'Expansión',
    'neg':'Negligible' if en else 'Despreciable',
    'dens_table':[
        ('Native, untreated' if en else 'Natural, sin tratar',1.93,'6.53%'),
        ('Treated 1:7' if en else 'Tratado 1:7',1.97,'6.62%'),
        ('Treated 1:8' if en else 'Tratado 1:8',1.96,'6.67%'),
        ('Treated 1:9' if en else 'Tratado 1:9',1.97,'6.48%')],
    'pq_text': ('"The native altered base measures 68 percent CBR. With the addition of the binder at a 1:7 ratio, it rises to 100 percent of the maximum dry density, meeting the minimum required for high-volume traffic under EG-2013."'
        if en else
        '"El CBR natural alterado es de 68 por ciento. Con la adición del aglutinante en proporción 1:7, sube al 100 por ciento de la máxima densidad seca, cumpliendo el mínimo requerido para tráfico de alto volumen según EG-2013."'),
    'pq_cite':'Technical conclusion, original report' if en else 'Conclusión técnica, informe original',
    # s4
    's4_eyebrow':'The Economics' if en else 'La Economía',
    's4_h':'Stronger ground, at a lower cost per square meter.' if en else 'Terreno más resistente, a menor costo por metro cuadrado.',
    's4_p': ("Because the binder converts the existing soil into the structural base, the conventional sub-base layer is eliminated and only a 15 cm base is required. The municipality compared the in-place method against the conventional build for the same corridor, on a 1,280 m² cost basis with tax (IGV) at 18 percent included."
        if en else
        "Como el aglutinante convierte el suelo existente en la base estructural, se elimina la sub-base convencional y solo se requiere una base de 15 cm. La municipalidad comparó el método in situ con la construcción convencional para la misma vía, sobre una base de costo de 1,280 m² con IGV al 18 por ciento incluido."),
    's4_cards':[
        ('S/ 78.66','Per m² with In-Place BaseGrade at 1:7' if en else 'Por m² con In-Place BaseGrade a 1:7'),
        ('S/ 83.88','Per m² with the conventional method' if en else 'Por m² con el método convencional'),
        ('6.22%','Cost reduction per square meter' if en else 'Reducción de costo por metro cuadrado'),
        ('S/ 6,679','Total saving on the project\'s direct cost' if en else 'Ahorro total en el costo directo')],
    's4_bA':'Budget A — In-Place BaseGrade (1:7)' if en else 'Presupuesto A — In-Place BaseGrade (1:7)',
    's4_bB':'Budget B — Conventional Method' if en else 'Presupuesto B — Método Convencional',
    'th_item':'Item' if en else 'Ítem','th_unit':'Unit' if en else 'Und','th_qty':'Quantity' if en else 'Metrado',
    'th_up':'Unit price S/' if en else 'Precio S/','th_sub':'Subtotal S/' if en else 'Parcial S/',
    'bA':[
        ('Base scarification, h = 0.15 m' if en else 'Escarificación de base, h = 0.15 m','m²','1,280.00','1.16','1,484.80'),
        ('Granular base, e = 15 cm' if en else 'Base granular, e = 15 cm','m²','1,280.00','41.96','53,708.80'),
        ('Asphalt priming' if en else 'Imprimación asfáltica','m²','1,280.00','4.82','6,169.60'),
        ('Cold-mix asphalt wear course, 2"' if en else 'Carpeta asfáltica en frío, 2"','m²','1,280.00','30.72','39,321.60')],
    'bA_tot':'Direct cost, tax included' if en else 'Costo directo, IGV incluido','bA_tot_v':'100,684.80',
    'bB':[
        ('Loose ground cut' if en else 'Corte de terreno suelto','m³','512.00','6.78','3,471.36'),
        ('Loose ground stockpiling' if en else 'Acopio de terreno suelto','m³','512.00','3.69','1,889.28'),
        ('Removal of cut surplus, up to 15 km' if en else 'Eliminación de excedente de corte, hasta 15 km','m³','665.60','18.75','12,480.00'),
        ('Subgrade shaping and compaction' if en else 'Perfilado y compactado de subrasante','m²','1,280.00','2.62','3,353.60'),
        ('Sub-base forming, 0.25 m' if en else 'Conformación de sub-base, 0.25 m','m²','1,280.00','18.75','24,000.00'),
        ('Granular base forming, 0.15 m' if en else 'Conformación de base granular, 0.15 m','m²','1,280.00','13.03','16,678.40'),
        ('Asphalt priming' if en else 'Imprimación asfáltica','m²','1,280.00','4.82','6,169.60'),
        ('Cold-mix asphalt wear course, 2"' if en else 'Carpeta asfáltica en frío, 2"','m²','1,280.00','30.72','39,321.60')],
    'bB_tot_v':'107,363.84',
    's4_note': ("The report notes the saving grows further for corridors longer than 1 km and in locations where no quarries exist nearby for forming bases and sub-bases, such as the upper reaches of the Arequipa sierra. It also observes that at a 1:8 ratio the saving would increase, since those proportions exceed 100 percent of the maximum dry density."
        if en else
        "El informe señala que el ahorro crece para vías de más de 1 km y en lugares donde no existen canteras cercanas para conformar bases y sub-bases, como las partes altas de la sierra de Arequipa. También observa que en proporción 1:8 el ahorro aumentaría, ya que esas proporciones superan el 100 por ciento de la máxima densidad seca."),
    # s5
    's5_eyebrow':'How It Was Built' if en else 'Cómo se Construyó',
    's5_h':'Mixed in place. No heat. No exotic equipment.' if en else 'Mezclado in situ. Sin calor. Sin equipos especiales.',
    'steps':[
        ('Subgrade preparation' if en else 'Preparación de la subrasante',
         "A motor grader scarified the base to a depth of 0.15 m. The material was not hauled off. The binder works with the soil already on site. Because the native soil was sandy silty with high moisture and absorption, 55 m³ of 1/2\" crushed stone was added so the mix could use less water and less binder while improving its physical and mechanical properties."
         if en else
         "Una motoniveladora escarificó la base a 0.15 m de profundidad. El material no se retiró de la obra. El aglutinante trabaja con el suelo existente. Como el suelo natural era arenoso limoso con alta humedad y absorción, se añadieron 55 m³ de piedra chancada de 1/2\" para usar menos agua y menos aglutinante a la vez que se mejoraban sus propiedades físico-mecánicas."),
        ('Mixing' if en else 'Mezclado',
         "In-Place BaseGrade is a flexible, water-borne solution that is 100 percent non-toxic. Mixing required no special handling by the crew and no heated temperature at any point. It was combined with water in cistern trucks at a 1:7 ratio, one part binder to seven parts water, dosed at 0.589 gallons per square meter. The project used 5,640 gallons of water and 755 gallons of binder, split across a 5,000 gallon cistern (4,300 water plus 575 binder) and a 2,500 gallon cistern (1,340 water plus 180 binder)."
         if en else
         "In-Place BaseGrade es una solución flexible a base de agua, 100 por ciento no tóxica. El mezclado no requirió cuidado especial del personal ni temperatura caliente en ningún momento. Se combinó con agua en camiones cisterna en proporción 1:7, una parte de aglutinante por siete de agua, dosificado a 0.589 galones por metro cuadrado. La obra usó 5,640 galones de agua y 755 de aglutinante, repartidos en una cisterna de 5,000 galones (4,300 de agua más 575 de aglutinante) y otra de 2,500 galones (1,340 de agua más 180 de aglutinante)."),
        ('Spreading and bonding' if en else 'Tendido y adherencia',
         "The binder was poured and blended into the scarified soil with the grader, watering, turning, and spreading at the same time until optimum moisture was reached. The water carries the binder into the soil, then retreats by capillary action, leaving the binder resins locked to the fines and gravels of the base."
         if en else
         "El aglutinante se vació y se mezcló con el suelo escarificado mediante la motoniveladora, regando, revolviendo y extendiendo a la vez hasta lograr la humedad óptima. El agua transporta el aglutinante hacia el suelo y luego se retira por capilaridad, dejando las resinas enlazadas con los finos y gravas de la base."),
        ('Compaction' if en else 'Compactación',
         "A vibratory compactor brought the mix to optimum density, stopping short of over-compaction. Mixing was completed within one hour and compaction within a two-hour window, since the material hardens quickly once the water leaves. Natural drying takes 24 to 72 hours, and the work needs to stay free of rain during this time. A single 8-hour shift covered 2,800 m², or 420 m³."
         if en else
         "Un compactador vibratorio llevó la mezcla a su densidad óptima, sin sobrecompactar. El mezclado se completó en una hora y la compactación dentro de una ventana de dos horas, pues el material endurece rápido al retirarse el agua. El secado natural toma de 24 a 72 horas y la obra debe permanecer libre de lluvia. Una jornada de 8 horas cubrió 2,800 m², o 420 m³."),
        ('Surface protection' if en else 'Protección de la superficie',
         "After curing, an MC-30 asphalt prime coat went down, followed by a 5 cm flexible pavement wear course. The treated base does not resist abrasion on its own, so it stays protected by the surface above it. Full strength is reached at 28 days. With this protection, the expected service life is approximately 10 to 15 years."
         if en else
         "Tras el curado se colocó una imprimación asfáltica MC-30 y luego una carpeta de pavimento flexible de 5 cm. La base tratada no resiste abrasión por sí sola, por lo que queda protegida por la superficie superior. La máxima resistencia se alcanza a los 28 días. Con esta protección, la vida útil estimada es de 10 a 15 años.")],
    's5_cap':[('In-place mixing with the motor grader' if en else 'Mezclado in situ con motoniveladora'),
              ('Binder and water blended in cistern trucks' if en else 'Aglutinante y agua mezclados en camiones cisterna'),
              ('Vibratory compaction of the treated base' if en else 'Compactación vibratoria de la base tratada')],
    # s6
    's6_eyebrow':'Quantities' if en else 'Metrados',
    's6_h':'Planned against built.' if en else 'Programado frente a ejecutado.',
    's6_p': ("The full bill of quantities, as programmed and as executed. The work was completed at 100 percent of the programmed scope, with the executed length and surfaced area slightly above plan."
        if en else
        "El metrado completo, programado y ejecutado. La obra se completó al 100 por ciento de lo programado, con la longitud y el área pavimentada ejecutadas ligeramente por encima de lo previsto."),
    'th_desc':'Description' if en else 'Descripción','th_prog':'Programmed' if en else 'Programado','th_exec':'Executed' if en else 'Ejecutado',
    'q_groups':[ (a if en else b) for a,b in [
        ('Provisional works and preliminaries','Obras provisionales y trabajos preliminares'),
        ('Flexible pavement, C-7 asphalt wear course','Pavimento flexible, carpeta asfáltica C-7'),
        ('Painting','Pintura'),('Miscellaneous','Varios')]],
    'q_rows':[ # (item, en_desc, es_desc, unit, prog, exec, group_index)
        ('01.01.01','Equipment mobilization and demobilization','Movilización y desmovilización de equipo','GLB','1.00','1.00',0),
        ('01.02.01','Collective protection equipment','Equipos de protección colectiva','GLB','1.00','1.00',0),
        ('01.02.02','Manual ground clearing','Limpieza de terreno manual','GLB','1.00','1.00',0),
        ('01.03.01','Manual ground clearing','Limpieza de terreno manual','m²','1,920.90','1,922.00',0),
        ('02.01','Cleaning of granular base surface','Limpieza de superficie de base granular','m²','1,920.90','1,922.00',1),
        ('02.02','Asphalt priming','Imprimación asfáltica','m²','1,920.90','1,922.00',1),
        ('02.03','Sanding, sweeping and surplus removal','Arenado, barrido y retiro de excedentes','m²','1,920.90','1,922.00',1),
        ('02.04','Cold-mix asphalt wear course, 2"','Carpeta asfáltica en frío, 2"','m²','1,920.90','1,922.00',1),
        ('03.01','Road marking','Señalización vial','m','300.14','310.00',2),
        ('03.02','Horizontal signage','Señalización horizontal','m²','50.00','50.00',2),
        ('04.01','Final cleaning','Limpieza final','m²','1,920.90','1,922.00',3),
        ('04.02','Traffic control','Control de tráfico','GLB','1.00','1.00',3)],
    's6_val':'Final Valuation of Works' if en else 'Valorización Final de Obra',
    'th_amt':'Amount S/' if en else 'Monto S/',
    'val_rows':[
        ('01.01.01','Mobilization and demobilization','Movilización y desmovilización','GLB','1.00','1,258.21','1,258.21'),
        ('01.02.01','Collective protection equipment','Equipos de protección colectiva','GLB','1.00','130.52','130.52'),
        ('01.02.02','Manual ground clearing','Limpieza de terreno manual','GLB','1.00','1,340.00','1,340.00'),
        ('01.03.01','Manual ground clearing','Limpieza de terreno manual','m²','1,920.90','0.92','1,767.23'),
        ('02.01','Cleaning of granular base surface','Limpieza de superficie de base granular','m²','1,920.90','1.28','2,458.75'),
        ('02.02','Asphalt priming','Imprimación asfáltica','m²','1,920.90','7.12','13,676.81'),
        ('02.03','Sanding, sweeping and surplus removal','Arenado, barrido y retiro de excedentes','m²','1,920.90','1.32','2,535.59'),
        ('02.04','Cold-mix asphalt wear course, 2"','Carpeta asfáltica en frío, 2"','m²','1,920.90','31.42','60,354.68'),
        ('03.01','Road marking','Señalización vial','m','300.14','4.21','1,263.59'),
        ('03.02','Horizontal signage','Señalización horizontal','m²','50.00','17.53','876.50'),
        ('04.01','Final cleaning','Limpieza final','m²','1,920.90','0.72','1,383.05'),
        ('04.02','Traffic control','Control de tráfico','GLB','1.00','488.14','488.14')],
    'val_tot':[ (a if en else b,c) for a,b,c in [
        ('Direct cost','Costo directo','87,533.08'),
        ('General expenses (10%)','Gastos generales (10%)','8,753.31'),
        ('Total budget','Presupuesto total','96,286.39'),
        ('Percentage complete','Porcentaje de avance','100.00%')]],
    # s7
    's7_eyebrow':'Resources' if en else 'Recursos',
    's7_h':'Valued summary of labor, materials, and equipment.' if en else 'Resumen valorizado de mano de obra, materiales y equipos.',
    's7_p': ("What the project actually consumed, set against what was budgeted. The difference between the two is the budget balance returned to the municipality."
        if en else
        "Lo que la obra realmente consumió, frente a lo presupuestado. La diferencia entre ambos es el saldo devuelto a la municipalidad."),
    's7_mat':'Materials Used' if en else 'Materiales Utilizados',
    'mat_rows':[
        ('MC-30 asphalt','Asfalto MC-30','gal','672.00','11.80','7,929.60'),
        ('RC-250 liquid asphalt','Asfalto líquido RC-250','gal','3,098.00','10.50','32,529.00'),
        ('Fine sand','Arena fina','m³','11.00','65.00','715.00'),
        ('Coarse sand','Arena gruesa','m³','96.00','45.00','4,320.00'),
        ('Screened stone, 2"','Piedra zarandeada, 2"','m³','59.00','79.00','4,661.00'),
        ('Signage tape, per 200 m','Cinta de señalización, por 200 m','und','2.00','48.00','96.00'),
        ('Traffic paint','Pintura de tráfico','gal','12.00','72.00','864.00'),
        ('Paint solvent','Disolvente para pintura','gal','4.50','33.78','152.01'),
        ('Diesel B5','Diésel B5','gal','465.00','12.11','5,631.15')],
    'mat_sub':'Materials subtotal' if en else 'Subtotal materiales','mat_sub_v':'56,897.76',
    's7_eq':'Equipment and Services' if en else 'Equipos y Servicios',
    'eq_rows':[
        ('Primer truck rental','Alquiler camión imprimador','h-m','4.00','180.00','720.00'),
        ('Pneumatic roller rental','Alquiler rodillo neumático','h-m','11.00','220.00','2,420.00'),
        ('Tandem roller rental','Alquiler rodillo tándem','h-m','8.00','220.00','1,760.00')],
    'eq_sub':'Equipment subtotal' if en else 'Subtotal equipos','eq_sub_v':'4,900.00',
    's7_tot':'Project Totals' if en else 'Totales del Proyecto',
    'th_used':'Used S/' if en else 'Utilizado S/','th_budg':'Budgeted S/' if en else 'Presupuestado S/',
    'tot_rows':[ (a if en else b,c,d) for a,b,c,d in [
        ('Labor','Mano de obra','8,500.00','8,709.59'),
        ('Materials','Materiales','56,897.76','63,390.46'),
        ('Equipment and services','Equipos y servicios','4,900.00','15,433.03'),
        ('General expenses','Gastos generales','0.00','8,753.31')]],
    'tot_total':'Total' if en else 'Total','tot_total_u':'70,297.76','tot_total_b':'96,286.39',
    'tot_bal':'Balance' if en else 'Saldo','tot_bal_v':'S/ 25,988.63',
    # s8
    's8_eyebrow':'The Verdict' if en else 'El Veredicto',
    's8_h':'Beneficial for the road, and for every road after it.' if en else 'Beneficioso para la vía, y para toda vía futura.',
    's8_lead': ("Applied at the 1:7 ratio with a dosage of 0.589 gallons per square meter, the result was economically sound, reducing direct cost by 6.22 percent per square meter while structurally increasing the density of the native soil."
        if en else
        "Aplicado en proporción 1:7 con una dosificación de 0.589 galones por metro cuadrado, el resultado fue rentable, reduciendo el costo directo en 6.22 por ciento por metro cuadrado a la vez que aumentaba estructuralmente la densidad del suelo natural."),
    's8_p1': ("Under the EG-2013 road manual, a CBR referred to 100 percent of the maximum dry density at 0.1\" penetration must be at least 100 percent for the TP6 high-volume traffic class, which works out to 1,702,886 ESAL for this corridor. The native altered base measured 68 percent. With the binder at 1:7 it rose to 100 percent of the maximum dry density, and richer ratios carried it well beyond."
        if en else
        "Según el manual de carreteras EG-2013, el CBR referido al 100 por ciento de la máxima densidad seca a 0.1\" de penetración debe ser al menos 100 por ciento para la clase TP6 de alto volumen, lo que equivale a 1,702,886 EE para esta vía. La base natural alterada midió 68 por ciento. Con el aglutinante a 1:7 subió al 100 por ciento de la máxima densidad seca, y las proporciones más ricas la llevaron mucho más allá."),
    's8_p2': ("The municipality's report closes on a forward-looking note: the treatment does not just serve this corridor, it raises the structural value of the ground itself, which is a benefit for any future pavement built on the same base. The work was completed at 100 percent of the programmed physical scope, with a budget balance of S/ 25,988.63 returned against the approved figure of S/ 96,286.39."
        if en else
        "El informe municipal cierra con una nota prospectiva: el tratamiento no solo sirve a esta vía, eleva el valor estructural del propio terreno, lo cual beneficia a cualquier pavimento futuro sobre la misma base. La obra se completó al 100 por ciento del alcance físico programado, con un saldo de S/ 25,988.63 devuelto frente a la cifra aprobada de S/ 96,286.39."),
    # s9
    's9_eyebrow':'Field Photography' if en else 'Panel Fotográfico',
    's9_h':'The complete photographic panel.' if en else 'El panel fotográfico completo.',
    's9_p': ("Every photograph from the original report, from site clearing through final road marking, in sequence."
        if en else
        "Cada fotografía del informe original, desde la limpieza del terreno hasta la señalización final, en secuencia."),
    # s10
    's10_eyebrow':'Engineering Drawings' if en else 'Planos',
    's10_h':'Plan and profile.' if en else 'Planta y perfil.',
    's10_c1':'Plan view, carriageway parallel to the Arequipa to Yura road, near Rodríguez Ballón airport' if en else 'Planta, vía carrozable paralela a la vía Arequipa - Yura, cerca del aeropuerto Rodríguez Ballón',
    's10_c2':'Grade profile, Calle 8. Horizontal scale 1:1000, vertical scale 1:100' if en else 'Perfil rasante, Calle 8. Escala horizontal 1:1000, vertical 1:100',
    # s11
    's11_eyebrow':'Appendix' if en else 'Anexo',
    's11_h':'The signed laboratory certificates.' if en else 'Los certificados de laboratorio firmados.',
    's11_p': ("All twelve CBR certificate pages from Roberto Cáceres Flores S.R.L., reproduced in full. Four mixes, three sheets each: the load and penetration curve, the raw density, moisture, expansion and penetration data, and the density versus CBR summary."
        if en else
        "Las doce páginas de certificados CBR de Roberto Cáceres Flores S.R.L., reproducidas íntegras. Cuatro mezclas, tres hojas cada una: la curva de carga y penetración, los datos de densidad, humedad, expansión y penetración, y el resumen de densidad frente a CBR."),
    'footer_tag':'Your Groundwork Strategist' if en else 'Su Estratega de Cimentación',
    'footer_cred':('Cerro Colorado, Peru / 2018<br>Complete Field Study and Translation' if en else 'Cerro Colorado, Perú / 2018<br>Estudio de Campo Completo y Traducción'),
    'footer_disc':("Translated and redesigned in full from the final engineering report of the Municipality of Cerro Colorado, Arequipa, Peru. Independent CBR testing by Roberto Cáceres Flores S.R.L., accredited to ISO/IEC 17025. All measurements reproduced as recorded. The product, described in the original report as a polymer, is a certified 100 percent organic binder."
        if en else
        "Traducido y rediseñado íntegramente del informe final de ingeniería de la Municipalidad de Cerro Colorado, Arequipa, Perú. Ensayos CBR independientes por Roberto Cáceres Flores S.R.L., acreditado ISO/IEC 17025. Todas las mediciones reproducidas como fueron registradas. El producto, descrito en el informe original como polímero, es un aglutinante certificado 100% orgánico."),
    }

# photo captions (key, en, es)
PHOTOS = [
 ('pg29_1','Site clearing','Limpieza de terreno'),
 ('pg29_2','Grade and level staking','Trazo de niveles'),
 ('pg29_3','Layout and setting out','Trazo y replanteo'),
 ('pg29_4','Layout and setting out','Trazo y replanteo'),
 ('pg29_5','Traffic control','Control de tráfico'),
 ('pg29_6','Traffic control','Control de tráfico'),
 ('pg10_1','In-place mixing with the motor grader','Mezclado con motoniveladora'),
 ('pg11_1','Binder and water blended in cistern trucks','Mezclado en camiones cisterna'),
 ('pg12_1','Vibratory compaction of the treated base','Compactación del suelo mezclado'),
 ('pg14_1','A rammed sample of the cured material','Muestra del material endurecido'),
 ('pg30_1','MC-30 asphalt prime coat','Imprimación con MC-30'),
 ('pg30_2','MC-30 asphalt prime coat','Imprimación con MC-30'),
 ('pg30_3','Traffic control','Control de tráfico'),
 ('pg30_4','Traffic control','Control de tráfico'),
 ('pg30_5','Sanding over MC-30 after three hours','Arenado encima de MC-30, después de 03 horas'),
 ('pg30_6','Sweeping and cleaning before the wear course','Barrido y limpieza antes de la carpeta'),
 ('pg13_1','Finished base ready for surfacing','Vía terminada lista para carpeteo'),
 ('pg31_1','Cold-mix asphalt wear course','Mantenimiento de carpeta asfáltica'),
 ('pg31_2','Cold-mix asphalt wear course','Mantenimiento de carpeta asfáltica'),
 ('pg31_3','Sanding the asphalt surface','Arenado de la carpeta asfáltica'),
 ('pg31_4','Sanding the asphalt surface','Arenado de la carpeta asfáltica'),
 ('pg31_5','Cleaning and road marking','Limpieza y señalización vial'),
 ('pg31_6','Cleaning and road marking','Limpieza y señalización vial'),
]
CERTS = [
 ('cert19',0,0),('cert18',0,1),('cert17',0,2),
 ('cert22',1,0),('cert21',1,1),('cert20',1,2),
 ('cert23',2,0),('cert24',2,1),('cert25',2,2),
 ('cert28',3,0),('cert27',3,1),('cert26',3,2),
]
def cert_caps(en):
    mix = (['Native base, untreated','Treated 1:7','Treated 1:8','Treated 1:9'] if en else
           ['Base natural, sin tratar','Tratado 1:7','Tratado 1:8','Tratado 1:9'])
    cbr = ['68%','98%','120%','125%']
    if en:
        sheet=['Load vs penetration curve (1 of 3)','Density, moisture, expansion, penetration (2 of 3)','Density vs CBR summary (3 of 3) — CBR {c}']
    else:
        sheet=['Curva carga-penetración (1 de 3)','Densidad, humedad, expansión y penetración (2 de 3)','Densidad vs CBR, resumen (3 de 3) — CBR {c}']
    out=[]
    for key,mi,si in CERTS:
        s=sheet[si].replace('{c}',cbr[mi])
        out.append((key,mix[mi],s))
    return out

def num(v): return f'<td class="num">{v}</td>'

def full_report(lang, idp):
    t=L(lang); en=lang=='en'
    H=[]
    # cover
    H.append(f"""<section class="section doc-head"><div class="container">
    <div class="eyebrow">{t['fr_eyebrow']}</div>
    <h2 class="doc-title">Cerro Colorado, {'Peru' if en else 'Perú'} <span>{'Full Engineering Report' if en else 'Informe de Ingeniería Completo'}</span></h2>
    <p style="max-width:760px;">{t['fr_sub']}</p>
    <div class="doc-meta">
      <div class="doc-meta-cell"><div class="doc-meta-k">{t['m_loc']}</div><div class="doc-meta-v">{t['m_loc_v']}</div></div>
      <div class="doc-meta-cell"><div class="doc-meta-k">{t['m_year']}</div><div class="doc-meta-v">2018</div></div>
      <div class="doc-meta-cell"><div class="doc-meta-k">{t['m_area']}</div><div class="doc-meta-v">1,922 m&sup2;</div></div>
      <div class="doc-meta-cell"><div class="doc-meta-k">{t['m_owner']}</div><div class="doc-meta-v">{t['m_owner_v']}</div></div>
    </div></div></section>""")
    # toc
    toc=''.join(f'<a class="toc-item" href="#{idp}s{i+1}"><span class="toc-n">{i+1:02d}</span><span class="toc-t">{x}</span></a>' for i,x in enumerate(t['toc']))
    H.append(f'<nav class="toc"><div class="toc-inner"><div class="toc-grid">{toc}</div></div></nav>')
    # preface
    H.append(f'<section class="section"><div class="container"><div class="preface"><div class="preface-label">{t["pre_label"]}</div><p>{t["pre_p1"]}</p><p>{t["pre_p2"]}</p></div></div></section>')
    # s1
    rows=''
    for name,sub,val,cls,w in t['cbr_rows']:
        rows+=f'<div class="tr"><div class="tr-name"><b>{name}</b>{sub}</div><div class="tr-val-wrap"><div class="tr-val">{val}<small>%</small></div></div><div class="tr-bar-wrap"><div class="tr-bar {cls}" data-w="{w}"></div></div></div>'
    H.append(f"""<section class="section section-dark section-num-outer" id="{idp}s1"><div class="section-ghost-num">01</div><div class="container">
    <div class="eyebrow">{t['s1_eyebrow']}</div><h2>{t['s1_h']}</h2><p class="lead">{t['s1_lead']}</p>
    <div class="tb"><div class="tb-label">{t['tb_label']}</div>{rows}<div class="tb-threshold">{t['tb_thresh']}</div></div>
    <p>{t['s1_p']}</p></div></section>""")
    # s2
    cards=''.join(f'<div class="dc"><div class="dc-num">{n}<span style="font-size:.5em">{u}</span></div><div class="dc-label">{l}</div></div>' for n,u,l in t['s2_stats'])
    rec=''.join(f'<tr><th>{k}</th><td>{"<span style=\'color:var(--rust);font-weight:600\'>"+v+"</span>" if k in (t["rec"][-1][0],) else v}</td></tr>' for k,v in t['rec'])
    H.append(f"""<section class="section section-num-outer" id="{idp}s2"><div class="section-ghost-num">02</div><div class="container">
    <div class="eyebrow">{t['s2_eyebrow']}</div><h2>{t['s2_h']}</h2><p>{t['s2_p']}</p>
    <div class="dc-grid">{cards}</div><h3>{t['s2_record']}</h3>
    <div class="table-wrap"><table class="lt"><tbody>{rec}</tbody></table></div></div></section>""")
    # s3
    cred=''.join(f'<div><div class="cred-k">{k}</div><div class="cred-v">{v}</div></div>' for k,v in t['cred'])
    cbr_t=''.join(f'<tr><td>{r[0]}</td>{num(r[1])}{num(r[2])}{num(r[3])}<td class="num hi">{r[4]}</td>{num(r[5])}</tr>' for r in t['cbr_table'])
    dens_t=''.join(f'<tr><td>{r[0]}</td>{num(r[1])}{num(r[2])}<td class="num">{t["neg"]}</td></tr>' for r in t['dens_table'])
    H.append(f"""<section class="section section-alt section-num-outer" id="{idp}s3"><div class="section-ghost-num">03</div><div class="container">
    <div class="eyebrow">{t['s3_eyebrow']}</div><h2>{t['s3_h']}</h2><p>{t['s3_p']}</p>
    <div class="cred"><div class="cred-org">{t['cred_org']}</div><div class="cred-name">Roberto Cáceres Flores S.R.L.</div>
    <p style="font-size:16px;color:var(--ink-mid);margin-bottom:0;">{t['cred_sub']}</p><div class="cred-grid">{cred}</div></div>
    <h3>{t['s3_t1']}</h3><div class="table-wrap"><table class="lt"><thead><tr><th>{t['th_mix']}</th><th class="num">12 {t['th_blows']}</th><th class="num">25 {t['th_blows']}</th><th class="num">56 {t['th_blows']}</th><th class="num">{t['th_cbr100']}</th><th class="num">{t['th_cbr95']}</th></tr></thead><tbody>{cbr_t}</tbody></table></div>
    <h3>{t['s3_t2']}</h3><div class="table-wrap"><table class="lt"><thead><tr><th>{t['th_mix']}</th><th class="num">{t['th_mdd']}</th><th class="num">{t['th_moist']}</th><th class="num">{t['th_exp']}</th></tr></thead><tbody>{dens_t}</tbody></table></div>
    <div class="pq"><p>{t['pq_text']}</p><cite>{t['pq_cite']}</cite></div></div></section>""")
    # s4
    cards=''.join(f'<div class="dc"><div class="dc-num">{n}</div><div class="dc-label">{l}</div></div>' for n,l in t['s4_cards'])
    def budget(rows,totlabel,totval):
        b=''.join(f'<tr><td>{r[0]}</td>{num(r[1])}{num(r[2])}{num(r[3])}{num(r[4])}</tr>' for r in rows)
        b+=f'<tr class="total"><td>{totlabel}</td><td></td><td></td><td></td>{num(totval)}</tr>'
        return f'<div class="table-wrap"><table class="lt"><thead><tr><th>{t["th_item"]}</th><th class="num">{t["th_unit"]}</th><th class="num">{t["th_qty"]}</th><th class="num">{t["th_up"]}</th><th class="num">{t["th_sub"]}</th></tr></thead><tbody>{b}</tbody></table></div>'
    H.append(f"""<section class="section section-num-outer" id="{idp}s4"><div class="section-ghost-num">04</div><div class="container">
    <div class="eyebrow">{t['s4_eyebrow']}</div><h2>{t['s4_h']}</h2><p>{t['s4_p']}</p><div class="dc-grid">{cards}</div>
    <h3>{t['s4_bA']}</h3>{budget(t['bA'],t['bA_tot'],t['bA_tot_v'])}
    <h3>{t['s4_bB']}</h3>{budget(t['bB'],t['bA_tot'],t['bB_tot_v'])}
    <p style="font-size:15px;color:var(--ink-light);">{t['s4_note']}</p></div></section>""")
    # s5
    steps=''.join(f'<div class="ps"><div class="ps-num">{i+1}</div><div class="ps-body"><h3>{h}</h3><p>{p}</p></div></div>' for i,(h,p) in enumerate(t['steps']))
    gal=''.join(f'<figure>{im(k)}<figcaption>{c}</figcaption></figure>' for k,c in zip(['pg10_1','pg11_1','pg12_1'],t['s5_cap']))
    H.append(f"""<section class="section section-alt section-num-outer" id="{idp}s5"><div class="section-ghost-num">05</div><div class="container">
    <div class="eyebrow">{t['s5_eyebrow']}</div><h2>{t['s5_h']}</h2>{steps}<div class="gallery gal">{gal}</div></div></section>""")
    # s6
    qb=''
    last=-1
    for it,de,ds,u,pr,ex,gi in t['q_rows']:
        if gi!=last:
            qb+=f'<tr class="group"><td>{["01","02","03","04"][gi]}</td><td colspan="4">{t["q_groups"][gi]}</td></tr>'; last=gi
        desc=de if en else ds
        qb+=f'<tr><td>{it}</td><td>{desc}</td><td class="num">{u}</td>{num(pr)}{num(ex)}</tr>'
    vb=''.join(f'<tr><td>{it}</td><td>{(de if en else ds)}</td><td class="num">{u}</td>{num(q)}{num(p)}{num(a)}</tr>' for it,de,ds,u,q,p,a in t['val_rows'])
    for lbl,v in t['val_tot']:
        vb+=f'<tr class="total"><td colspan="5">{lbl}</td>{num(v)}</tr>'
    H.append(f"""<section class="section section-num-outer" id="{idp}s6"><div class="section-ghost-num">06</div><div class="container">
    <div class="eyebrow">{t['s6_eyebrow']}</div><h2>{t['s6_h']}</h2><p>{t['s6_p']}</p>
    <div class="table-wrap"><table class="lt"><thead><tr><th>{t['th_item']}</th><th>{t['th_desc']}</th><th class="num">{t['th_unit']}</th><th class="num">{t['th_prog']}</th><th class="num">{t['th_exec']}</th></tr></thead><tbody>{qb}</tbody></table></div>
    <h3>{t['s6_val']}</h3><div class="table-wrap"><table class="lt"><thead><tr><th>{t['th_item']}</th><th>{t['th_desc']}</th><th class="num">{t['th_unit']}</th><th class="num">{t['th_qty']}</th><th class="num">{t['th_up']}</th><th class="num">{t['th_amt']}</th></tr></thead><tbody>{vb}</tbody></table></div></div></section>""")
    # s7
    mat=''.join(f'<tr><td>{(e if en else s)}</td><td class="num">{u}</td>{num(q)}{num(p)}{num(a)}</tr>' for e,s,u,q,p,a in t['mat_rows'])
    mat+=f'<tr class="total"><td colspan="4">{t["mat_sub"]}</td>{num(t["mat_sub_v"])}</tr>'
    eq=''.join(f'<tr><td>{(e if en else s)}</td><td class="num">{u}</td>{num(q)}{num(p)}{num(a)}</tr>' for e,s,u,q,p,a in t['eq_rows'])
    eq+=f'<tr class="total"><td colspan="4">{t["eq_sub"]}</td>{num(t["eq_sub_v"])}</tr>'
    tot=''.join(f'<tr><td>{l}</td>{num(u)}{num(b)}</tr>' for l,u,b in t['tot_rows'])
    tot+=f'<tr class="total"><td>{t["tot_total"]}</td>{num(t["tot_total_u"])}{num(t["tot_total_b"])}</tr>'
    tot+=f'<tr class="total"><td>{t["tot_bal"]}</td><td class="num hi" colspan="2">{t["tot_bal_v"]}</td></tr>'
    H.append(f"""<section class="section section-alt section-num-outer" id="{idp}s7"><div class="section-ghost-num">07</div><div class="container">
    <div class="eyebrow">{t['s7_eyebrow']}</div><h2>{t['s7_h']}</h2><p>{t['s7_p']}</p>
    <h3>{t['s7_mat']}</h3><div class="table-wrap"><table class="lt"><thead><tr><th>{t['th_desc']}</th><th class="num">{t['th_unit']}</th><th class="num">{t['th_qty']}</th><th class="num">{t['th_up']}</th><th class="num">{t['th_amt']}</th></tr></thead><tbody>{mat}</tbody></table></div>
    <h3>{t['s7_eq']}</h3><div class="table-wrap"><table class="lt"><thead><tr><th>{t['th_desc']}</th><th class="num">{t['th_unit']}</th><th class="num">{t['th_qty']}</th><th class="num">{t['th_up']}</th><th class="num">{t['th_amt']}</th></tr></thead><tbody>{eq}</tbody></table></div>
    <h3>{t['s7_tot']}</h3><div class="table-wrap"><table class="lt"><thead><tr><th></th><th class="num">{t['th_used']}</th><th class="num">{t['th_budg']}</th></tr></thead><tbody>{tot}</tbody></table></div></div></section>""")
    # s8
    H.append(f"""<section class="section section-earth section-num-outer" id="{idp}s8"><div class="section-ghost-num">08</div><div class="container">
    <div class="eyebrow">{t['s8_eyebrow']}</div><h2>{t['s8_h']}</h2><p class="lead">{t['s8_lead']}</p><p>{t['s8_p1']}</p><p>{t['s8_p2']}</p></div></section>""")
    # s9 gallery
    gal=''.join(f'<figure>{im(k)}<figcaption>{(e if en else s)}<br><span class="ph">{(s if en else e)}</span></figcaption></figure>' for k,e,s in PHOTOS)
    H.append(f"""<section class="section section-num-outer" id="{idp}s9"><div class="section-ghost-num">09</div><div class="container">
    <div class="eyebrow">{t['s9_eyebrow']}</div><h2>{t['s9_h']}</h2><p>{t['s9_p']}</p><div class="gallery gal">{gal}</div></div></section>""")
    # s10 drawings
    H.append(f"""<section class="section section-stone section-num-outer" id="{idp}s10"><div class="section-ghost-num">10</div><div class="container">
    <div class="eyebrow">{t['s10_eyebrow']}</div><h2>{t['s10_h']}</h2>
    <figure class="fig">{im('draw32')}<figcaption>{t['s10_c1']}</figcaption></figure>
    <figure class="fig">{im('draw33')}<figcaption>{t['s10_c2']}</figcaption></figure></div></section>""")
    # s11 certs
    cg=''.join(f'<figure>{im(k,alt=mix)}<figcaption>{mix} &middot; {sheet}</figcaption></figure>' for k,mix,sheet in cert_caps(en))
    H.append(f"""<section class="section section-alt section-num-outer" id="{idp}s11"><div class="section-ghost-num">11</div><div class="container">
    <div class="eyebrow">{t['s11_eyebrow']}</div><h2>{t['s11_h']}</h2><p>{t['s11_p']}</p><div class="certgrid cert">{cg}</div></div></section>""")
    # footer
    H.append(f"""<footer class="footer"><div class="container"><div class="footer-inner">
    <div><div class="footer-brand">In-Place BaseGrade</div><div class="footer-tag">{t['footer_tag']}</div><div class="footer-cred">{t['footer_cred']}</div></div>
    <div class="footer-disclaimer">{t['footer_disc']}</div></div>
    <div class="footer-copy">In-Place BaseGrade &middot; Evidence Series &middot; {'Complete Edition' if en else 'Edición Completa'}</div></div></footer>""")
    return '\n'.join(H)

def summary(lang):
    t=L(lang); en=lang=='en'
    eyebrow='Executive Summary' if en else 'Resumen Ejecutivo'
    h='A municipal road, treated in place, that beat the standard.' if en else 'Una vía municipal, tratada in situ, que superó el estándar.'
    lead=("In 2018 the Municipality of Cerro Colorado, in Arequipa, Peru, rebuilt a 310 meter stretch of the Añashuayco road by treating the existing soil in place with In-Place BaseGrade. An accredited laboratory measured the result against the worldwide CBR standard. The native base scored 68 percent, below the 100 percent that Peru's road manual demands for this heavy-traffic class. Treated, the same ground rose to between 98 and 125 percent, and it cost 6.22 percent less per square meter than a conventional build because no sub-base was needed."
        if en else
        "En 2018 la Municipalidad de Cerro Colorado, en Arequipa, Perú, reconstruyó 310 metros de la vía Añashuayco tratando el suelo existente in situ con In-Place BaseGrade. Un laboratorio acreditado midió el resultado frente al estándar mundial CBR. La base natural alcanzó 68 por ciento, por debajo del 100 por ciento que exige el manual de carreteras del Perú para esta clase de tráfico pesado. Tratado, el mismo terreno subió a entre 98 y 125 por ciento, y costó 6.22 por ciento menos por metro cuadrado que una construcción convencional porque no se necesitó sub-base.")
    stats=[('68 to 125','%','CBR, native versus treated' if en else 'CBR, natural frente a tratado'),
           ('6.22','%','Lower cost per square meter' if en else 'Menor costo por metro cuadrado'),
           ('102','%','Field compaction grade' if en else 'Grado de compactación en campo'),
           ('10-15',('yrs' if en else 'años'),'Expected service life' if en else 'Vida útil estimada')]
    cards=''.join(f'<div class="dc"><div class="dc-num">{n}<span style="font-size:.5em">{u}</span></div><div class="dc-label">{l}</div></div>' for n,u,l in stats)
    rows=''
    for name,sub,val,cls,w in t['cbr_rows']:
        rows+=f'<div class="tr"><div class="tr-name"><b>{name}</b>{sub}</div><div class="tr-val-wrap"><div class="tr-val">{val}<small>%</small></div></div><div class="tr-bar-wrap"><div class="tr-bar {cls}" data-w="{w}"></div></div></div>'
    costcards=''.join(f'<div class="dc"><div class="dc-num">{n}</div><div class="dc-label">{l}</div></div>' for n,l in t['s4_cards'])
    gal=''.join(f'<figure>{im(k)}<figcaption>{c}</figcaption></figure>' for k,c in zip(['pg10_1','pg12_1','pg13_1'], (t['s5_cap'][:2]+[('Finished base ready for surfacing' if en else 'Vía terminada lista para carpeteo')])))
    close=("Applied at a 1:7 ratio and protected by a thin asphalt wear course, the treated base is expected to last 10 to 15 years. The full report, the cost breakdowns, the construction record, the field photography, and all twelve signed laboratory certificates are in the Full Report tab."
        if en else
        "Aplicado en proporción 1:7 y protegido por una delgada carpeta asfáltica, se espera que la base tratada dure de 10 a 15 años. El informe completo, los desgloses de costos, el registro de obra, el panel fotográfico y los doce certificados de laboratorio firmados están en la pestaña de Informe Completo.")
    return f"""<section class="section doc-head"><div class="container">
    <div class="eyebrow">{eyebrow}</div>
    <h2 class="doc-title">Cerro Colorado, {'Peru' if en else 'Perú'} <span>{'Summary' if en else 'Resumen'}</span></h2>
    <p class="lead">{lead}</p></div></section>
    <section class="section"><div class="container">
      <div class="dc-grid">{cards}</div>
      <div class="tb"><div class="tb-label">{t['tb_label']}</div>{rows}<div class="tb-threshold">{t['tb_thresh']}</div></div>
      <h3>{t['s4_eyebrow']}</h3><div class="dc-grid">{costcards}</div>
      <div class="gallery gal">{gal}</div>
      <p class="lead" style="margin-top:8px;">{close}</p>
    </div></section>"""

HERO_HEAD = """<section class="summary-hero cover"><div class="cover-diagonal"></div><div class="cover-inner">
<div class="cover-wordmark">IN-PLACE BASEGRADE<span>Your Groundwork Strategist</span></div>
<div class="cover-eyebrow">Field Evidence / Evidencia de Campo</div>
<h1 class="cover-h1">Cerro Colorado, Peru</h1>
<p class="cover-sub">A municipal road in the Arequipa highlands, treated in place to a structural base and independently tested against the worldwide CBR standard. The native ground scored 68 percent CBR, below the threshold for heavy traffic. Treated with In-Place BaseGrade, it rose to between 98 and 125 percent, at 6.22 percent lower cost than a conventional build. Choose a tab below for the full report or a summary, in English or Spanish.</p>
</div></section>"""

TABS = """<nav class="tabs-bar"><div class="tabs-inner">
<button class="tab-btn active" data-tab="enfull">Full Report<span>English</span></button>
<button class="tab-btn" data-tab="ensum">Summary<span>English</span></button>
<button class="tab-btn" data-tab="esfull">Informe Completo<span>Español</span></button>
<button class="tab-btn" data-tab="essum">Resumen<span>Español</span></button>
</div></nav>"""

panels = (
 f'<div class="tab-panel active" id="enfull">{full_report("en","en")}</div>'
 f'<div class="tab-panel" id="ensum">{summary("en")}</div>'
 f'<div class="tab-panel" id="esfull">{full_report("es","es")}</div>'
 f'<div class="tab-panel" id="essum">{summary("es")}</div>'
)

HTML = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cerro Colorado, Peru \u2014 In-Place BaseGrade</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;1,700&family=Barlow:opsz,wght@6..14,300;6..14,400;6..14,500;6..14,600&family=Barlow+Condensed:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head><body>
{HERO_HEAD}
{TABS}
<main>{panels}</main>
<script src="assets/js/app.js"></script>
</body></html>"""

out=os.path.join(ROOT,'index.html')
open(out,'w',encoding='utf-8').write(HTML)
print('Wrote', out, '(', round(len(HTML.encode())/1024), 'KB )')
