package diseasediagnosis;

import com.hp.hpl.jena.rdf.model.Model;
import com.hp.hpl.jena.rdf.model.ModelFactory;
import org.apache.jena.riot.Lang;
import org.apache.jena.riot.RDFDataMgr;
import org.apache.jena.riot.RDFFormat;

public class DiseaseDiagnosis {

    public static void main(String[] args) {

        Model model = ModelFactory.createDefaultModel();
        model.read("src/jsonld/diseases.jsonld", "JSON-LD");

        // Write a model in Turtle syntax, default style (pretty printed)
        RDFDataMgr.write(System.out, model, Lang.JSONLD);

        // Wriet Turtle to the blocks variant
        RDFDataMgr.write(System.out, model, RDFFormat.JSONLD_PRETTY);

        // Write as Turtle via model.write
        model.write(System.out, "JSONLD");

    }

}
