from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/2d', methods=['GET', 'POST'])
def two_d_shapes():
    result = None 
    if request.method == 'POST':
        inpulu = int(request.form['shape'])  
        calc_type = request.form.get('calculation')

        # RECTANGLE AREA
        if inpulu == 1:
            try:
                rech = float(request.form['length'])  
                recw = float(request.form['width'])  
                if calc_type == 'area':
                    reca = rech * recw
                    result = f"The area of the rectangle is: {reca} square units"
                elif calc_type == 'perimeter':
                    recp = 2*(rech+recw)
                    result = f"The perimeter of the rectangle is: {recp} units"
            
            except ValueError:
                result = "Invalid input! Please enter valid numbers for length and width."
        
        # TRIANGLE AREA
        elif inpulu == 2:
            if calc_type == 'area':
                try:
                    trih = float(request.form['height'])  
                    trib = float(request.form['base'])   
                    tria = (trih * trib) / 2
                    result = f"The area of the triangle is: {tria} square units"
                except ValueError:
                    result = "Invalid input! Please enter valid numbers for height and base."
            elif calc_type == 'perimeter':
                try: 
                    side1 = float(request.form['side 1'])
                    side2 = float(request.form['side 2'])
                    side3 = float(request.form['side 3'])
                    trip = side1 + side2 + side3
                    result = f"The perimeter of the triangle is: {trip} units"
                except ValueError:
                    result = "Invalid input! Please enter valid numbers for all three sides."

        # CIRCLE AREA
        elif inpulu == 3:
            radiordia = request.form['radius_or_diameter']
            if calc_type == 'area':
                if radiordia == 'radius':
                    try:
                        cirr = float(request.form['radius'])
                        cira = math.pi * cirr ** 2
                        result = f"The area of the circle is: {cira} square units"
                    except ValueError:
                        result = "Invalid input! Please enter a valid number for the radius."
                elif radiordia == 'diameter':
                    try:
                        cird = float(request.form['diameter'])
                        cira2 = math.pi * (cird / 2) ** 2
                        result = f"The area of the circle is: {cira2} square units"
                    except ValueError:
                        result = "Invalid input! Please enter a valid number for the diameter."
            elif calc_type == 'perimeter':  # Circumference
                if radiordia == 'radius':
                    try:
                        cirr = float(request.form['radius'])
                        circ = 2 * math.pi * cirr
                        result = f"The circumference of the circle is: {circ} units"
                    except ValueError:
                        result = "Invalid input! Please enter a valid number for the radius."
                elif radiordia == 'diameter':
                    try:
                        cird = float(request.form['diameter'])
                        circ = math.pi * cird
                        result = f"The circumference of the circle is: {circ} units"
                    except ValueError:
                        result = "Invalid input! Please enter a valid number for the diameter."

    return render_template('2d.html', result=result)

@app.route('/3d', methods=['GET', 'POST'])
def three_d_shapes():
    result1 = None
    inputs = {}

    if request.method == 'POST':
        inputs = {key: request.form.get(key, '') for key in request.form}

        try:
            shape = inputs.get('shape')

            if shape == 'cube':
                length = float(inputs['cube_length'])
                volume = length ** 3
                result1 = f"The volume of the cube is: {volume:.2f} cubic units"

            elif shape == 'cylinder':
                radius = float(inputs['cylinder_radius'])
                height = float(inputs['cylinder_height'])
                volume = math.pi * (radius ** 2) * height
                result1 = f"The volume of the cylinder is: {volume:.2f} cubic units"

            elif shape == 'rectangular_prism':
                length = float(inputs['rectangular_prism_length'])
                width = float(inputs['rectangular_prism_width'])
                height = float(inputs['rectangular_prism_height'])
                volume = length * width * height
                result1 = f"The volume of the rectangular prism is: {volume:.2f} cubic units"

            elif shape == 'triangular_prism':
                length = float(inputs['triangular_prism_length'])
                width = float(inputs['triangular_prism_width'])
                height = float(inputs['triangular_prism_height'])
                volume = 0.5 * width * height * length
                result1 = f"The volume of the triangular prism is: {volume:.2f} cubic units"

            elif shape == 'cone':
                radius = float(inputs['cone_radius'])
                height = float(inputs['cone_height'])
                volume = (1/3) * math.pi * (radius ** 2) * height
                result1 = f"The volume of the cone is: {volume:.2f} cubic units"

            elif shape == 'sphere':
                radius = float(inputs['sphere_radius'])
                volume = (4/3) * math.pi * (radius ** 3)
                result1 = f"The volume of the sphere is: {volume:.2f} cubic units"

            elif shape == 'triangular_pyramid':
                base = float(inputs['triangular_pyramid_base'])
                height_base = float(inputs['triangular_pyramid_height_base'])
                height = float(inputs['triangular_pyramid_height'])
                base_area = 0.5 * base * height_base
                volume = base_area * height / 3
                result1 = f"The volume of the triangular pyramid is: {volume:.2f} cubic units"

            elif shape == 'rectangular_pyramid':
                base = float(inputs['rectangular_pyramid_base'])
                height_base = float(inputs['rectangular_pyramid_height_base'])
                height = float(inputs['rectangular_pyramid_height'])
                base_area = base * height_base
                volume = base_area * height / 3
                result1 = f"The volume of the rectangular pyramid is: {volume:.2f} cubic units"

            else:
                result1 = "Invalid shape selected."
        except ValueError:
            result1 = "Invalid input! Please enter valid numbers."

    return render_template('3d.html', result1=result1, inputs=inputs)

@app.route('/pythagorean', methods=['GET', 'POST'])
def pythagorean():
    result2 = None
    if request.method == 'POST':
        try:
            side = request.form['side']  
            if side == '1':  
                leg1 = float(request.form['leg1'])
                leg2 = float(request.form['leg2'])
                goofy = round((leg1**2 + leg2**2)**0.5, 2)
                result2 = f"Hypotenuse: {goofy} units"
            elif side == '2':  
                hypotenuse = float(request.form['hypotenuse'])
                leg1 = float(request.form['leg1'])
                goofy = round((hypotenuse**2 - leg1**2)**0.5, 2)
                result2 = f"Missing Leg: {goofy} units"
        except KeyError as e:
            result2 = f"Missing input field: {e.args[0]}"
        except ValueError:
            result2 = "Invalid input. Please enter valid numbers."
    return render_template('pythagorean.html', result2=result2)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
