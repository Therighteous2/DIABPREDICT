import streamlit as st
from PIL import Image

st.title("INFORMATIONS SUR LE DIABETE")
st.markdown("___")
st.subheader("C'est quoi le diabète ?")
st.markdown("""Le diabète est l'une des maladies les plus courantes dans le monde, on estime que 800 millions de personnes dans le monde
            souffrent de cette maladie et 1,4 millions de personnes en R.D.Congo en 2023, sans compter celles qui ne le savent pas encore!
            Cette maladie est reputée d'être  *une maladie silencieuse* car l'une de ses variantes peut être présente chez un patient sans 
            aucune manifestation des symptômes pendant des années!
            Le diabète sucré est une maladie grave, à long terme (ou chronique) qui survient chez un patient lorsque le taux de glycémie (ou sucre dans le sang)
            est élevé parce que son organisme ne peut pas produire assez d'insuline, qu'il n'en produit pas ou qu'il ne peut pas utiliser efficacement l'insuline qu'il produit.
""")
col1,col2 = st.columns([2,1])
with col1:
    st.subheader("Et l'insuline qu'est-ce?")
    st.markdown(""" Brièvement, le diabète est la quantité élevée du sucre dans le sang; le sucre est le glucose, et la quantité du glucose dans le sang s'appelle **la glycémie.**
                 Le glucose est un peu comme notre carburant, ça nous permet de faire de l'énergie: quand on mange, on fait le plein! Avec les aliments que nous mangeons, la digestion produit
                 du glucose qui est transporté dans le sang, c'est à l'intérieur des cellules que le glucose se transforme en énergie et pour *le faire entrer*, on a besoin de **l'insuline.**
                L'insuline est une hormone produit dans le pancréas (un organe qui se trouve derrière l'estomac). Quand on mange, le pancréas envoie de l'insuline dans le sang et cela permet
                au glucose d'entrer dans les cellules pour faire de l'énergie. En cas de diabète, le système est déreglé: le glucose s'accumule dans le sang et ça provoque des problèmes.
                 
""")

with col2:
    image = Image.open("C:/Users/windows 10/Desktop/MyProject/images/image1.jpeg")
    st.markdown("___________")
    st.image(image, caption ="Insuline",width=400)
st.subheader("Les types de diabète")
st.markdown(""" En général, on distingue deux types de diabète: le diabète de type 1 (DT1) et le diabète de type 2 (DT2), mais il éxiste aussi des types particuliers comme le diabète mitochondrial, 
            le diabète de MODY et le diabète gestationnel. Mais ici, nous parlerons que du DT1, DT2 et du diabète gestationnel.
""")
col3,col4 = st.columns([2,1])
with col3:
    st.subheader("1°. Le diabète de type 1")
    st.markdown(""" Le diabète de type 1 (DT1) aussi appelé **diabète insulino-dépendant**, est une maladie au cours duquel des cellules du pancréas sont détruites, entraînant ainsi une diminution
                 voire une absence totale de sécretion d'insuline; le glucose n'arrive donc plus à pénetrer dans les cellules, favorisant une augmentation du taux sanguin et provoquant une hyperglycémie.
                Ses symptômes comme les envies fréquentes d'uriner et une soif plus importante que d'ordinaire peut se manifester rapidement. Mais ils ne peuvent que marquer le début, cela peut évoluer
                 avec un amaigrissement, une fatigue, une sensation de faim intense. Tout ceci arrive très rapidement chez les enfants, et peut entraîner une déshydratation, des vomissemnts, des doumeurs
                abdominales, voire des malaises... 
                
""")
    st.write("**Diagnostic & Traitement**")
    st.markdown(""" Aux premiers symptômes évocateurs d'un diabète, particulièrement chez l'enfant, il est indispensable de consulter rapidement un professionnel de santé pour éviter les premières complications.
                 Le médecin traitant pourra faire le diagnostic par une prise de sang montrant une hyperglycémie à plus de 1,20 g/l. Celle-ci devra être constatée à au moins 2 reprises pour que le diabète soit averé.
                Le DT1 étant insulino-dépendant, il peut se traiter uniquement par des injections d'insuline. Ce nombre d'injections doit s'adapter tout au long de la maladie pour que le patient ait toujours assez d'insuline pour maintenir une glycémie
                normale ainsi qu'une hémoglobine glyquée inférieure à 7%.
""")
    st.subheader("2°. Le diabète de type 2")
    st.markdown(""" Le diabète de type 2 (DT2) se caracterise par une résistance à l'insuline, qui entraîne alors une augmentation importante de la glycémie c-à-d du taux de sucre dans le sang. c'est la forme du diabète la plus fréquente.
                 Il s'agit à l'origine de la maturité et du vieillissement, car il est favorisé par le surpoids, l'obésité ou la sedentarité. Ce type de diabète peut être silencieux pendant des années, des complications peuvent survenir d'un coup,
                 provoquant des lésions de différents organes, parfois irréversibles. Le DT2 n'est pas d'une pathologie auto-immune, au contraire il est dû à plusieurs facteurs : **Des facteurs génétiques**(antécédents familiaux), 
                **Des facteurs environnementaux**: une alimentation deséquilibrée, manque d'activité physique, surpoids ou encore des facteurs à risque associés tels que le tabagisme (actif ou passif). Les personnes sédentaires et en surpoids sont 
                les plus exposées à ce type de diabète. Cette maladie peut évoluer pendant des années sans provoquer aucun symptôme. Le DT2 ne se voit pas avant l'apparition des complications; les signes se présentent comme la fatigue, troubles de la vision,
                 sensation de la bouche sèche, besoins fréquents d'uriner, avoir excessivement faim ou soif, picotement dans les pieds, infections qui guérissent mal, etc. Tous ces signes apparaissent lentement.
    
""")
    st.write("**Diagnostic & Traitement**")
st.markdown(""" Une prise de sang en laboratoire permet de mésurer la glycémie dans le sang; un taux de glycémie à jeun supérieur ou égal à 1,26 g/l à deux reprises, diagnostique le diabète. D'autres dosages peuvent être réalisés: glycémie post-prandiale (2h après le repas),
                glycosurie (présence de sucre dans les urines), hémoglobine glycosylée, sont rarement utilisés pour le diagnostic de diabète mais peuvent aider au suivi. L'examen médical complet sera à la recherche de signes pouvant orienter sur l'origine du diabète et sur l'existence
                des complications: *évaluation de la surcharge pondérale (poids, taille, répartition des graisses), prise de la tension artérielle, auscultation du coeur et vaisseaux, examen des reflexes et la sensibilité des jambes et des pieds*
""")
st.subheader("3°. Le diabète gestationnel")
st.markdown(""" Le diabète gestationnel est un diabète qui survient chez une femme enceinte, du fait des modifications métaboliques provoquées par la grossesse (mais pas pour toutes les femmes). Il est aussi appelé *diabète de grossesse*; contrairement aux DT1 et DT2 qui sont des pathologies
            évolutives et à surveiller à vie, le diabète gestationnel disparaît le plus souvent après la naissance du bébé...
            Lorsqu'une femme souffre du diabète gestationnel au cours de sa grossesse, elle est exposée à un risque élevé de développer un DT2. **Plus une femme enceinte a un âge avancé, plus le risque de développer un diabète gestationnel au cours de sa grossesse est élevé.**
""")

with col4:
    image = Image.open("C:/Users/windows 10/Desktop/MyProject/images/DT1.jpg")
    st.image(image, width=400,caption="Diabète de type 1")
    st.markdown("___________")
    st.markdown("___________")
    st.markdown("___________")
    st.markdown("___________")
    st.markdown("___________")

    image1 = Image.open("C:/Users/windows 10/Desktop/MyProject/images/DT2.jpg")
    st.image(image1, width=400,caption="Diabète de type 2")

st.subheader("**Rélation du diabète avec l'hérédité et la grossesse**")
st.write("**1°. L'hérédité**")
st.markdown(""" Le poids de l'hérédité diffère selon qu'il s'agit du diabète du type 1 ou du type 2. Lorsque l'un des deux parents est diabétique de type 2, le risque de transmission à la descendance est de l'ordre de 40 % et si les deux parents sont atteints, le risque grimpe à
            70 %. Dans le cas du diabète de type 1, le risque se situe entre 4 % et 8 %, plus précisément 8 % si le père est diabétique, 4 % si c'est la mère (mais 30 % si les deux parents le sont). Il est donc utile de se construire un arbre généalogique pour repérer les membres
            de sa famille diabétique et connaître son patrimoine génétique.
""")
st.write("**2°. La grossesse**")
st.markdown("""Les femmes diabétiques sont plus à risque de fausse-couche ou d'avoir un bébé avec des malformations congénitales (malformations cardiaques et rénales par exemple). Ce risque augmente considérablement si le contrôle de la glycémie n'est pas optimal, surtout au moment
            de la conception et durant les 3 premiers mois de la grossesse; une glycémie mal contrôlée présente de nombreux risques pour la mère et le bébé. Bien se préparer pour une grossesse peut aider à réduire les risques de complications et à conserver une bonne santé pendant 
            toute la durée de la grossesse, en plus de donner un bon départ dans la vie à votre bébé.
""")


st.markdown("___________")
st.subheader("**Pour plus d'informations**")
st.markdown("**Féderation des diabétiques**  [Cliquez ici pour visiter](https://www.federationdesdiabetiques.org)")
st.markdown("**Organisation Mondiale de la santé**  [Cliquez ici pour visiter](https://www.who.int/fr/news-room/fact-sheets/detail/diabetes)")

st.sidebar.write("*Anticipez le diabète, protégez votre avenir!*")
st.sidebar.image('C:\\Users\\windows 10\\Desktop\\MyProject\\images\\logo.png',use_container_width=True)

